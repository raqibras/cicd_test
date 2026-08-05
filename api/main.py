import csv
from datetime import date
from io import StringIO

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse

from config import RESOURCE_GROUP_TO_PROJECT_MAPPING, INCLUDED_RESOURCE_GROUPS, RESOURCE_TO_PROJECT_MAPPING
from report_generator import aggregate_resource_costs, build_excel_report

app = FastAPI(title="Azure Cost Report API V5.0")

EXCEL_MEDIA_TYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"


def cost_per_application(csv_reader: csv.DictReader) -> dict:
    """Kept unchanged - existing project/application cost totals."""
    project_costs = {}

    for row in csv_reader:
        resource_group = row.get("ResourceGroupName")
        resource_name = row.get("Resource")

        if resource_group not in INCLUDED_RESOURCE_GROUPS:
            print(f"Resource group {resource_group} is not in the included list. Skipping.")
            continue

        if resource_name in RESOURCE_TO_PROJECT_MAPPING:
            project_name = RESOURCE_TO_PROJECT_MAPPING[resource_name]
            project_costs[project_name] = project_costs.get(project_name, 0.0) + float(str(row["Cost"]))

        elif resource_group in RESOURCE_GROUP_TO_PROJECT_MAPPING:
            project_name = RESOURCE_GROUP_TO_PROJECT_MAPPING[resource_group]
            project_costs[project_name] = project_costs.get(project_name, 0.0) + float(row.get("Cost", 0))

        else:
            print(f"No mapping found for resource group {resource_group} or resource {resource_name}. Skipping.")
            continue

    return project_costs


def _read_upload_as_csv(raw_bytes: bytes) -> csv.DictReader:
    """Decodes uploaded bytes (handling a BOM if present) into a DictReader."""
    try:
        decoded = raw_bytes.decode("utf-8-sig")
    except UnicodeDecodeError:
        decoded = raw_bytes.decode("latin-1")
    return csv.DictReader(StringIO(decoded))


@app.post("/cost-per-application")
async def cost_per_application_endpoint(file: UploadFile = File(...)):
    """Existing behaviour: aggregated cost totals per application, as JSON."""
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a .csv file.")

    raw_bytes = await file.read()
    csv_reader = _read_upload_as_csv(raw_bytes)
    project_costs = cost_per_application(csv_reader)

    if not project_costs:
        return JSONResponse(status_code=400, content={"error": "No matching data found in the uploaded CSV."})

    return {"project_costs": project_costs}


@app.post("/consolidated-report")
async def consolidated_report_endpoint(file: UploadFile = File(...)):
    """
    Accepts an Azure cost-export CSV, aggregates cost by Resource, and
    returns a consolidated .xlsx report with columns:
    SI No., Resource Name, Resource Group, Service, Application,
    Subscription, Location, Cost (USD).
    """
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a .csv file.")

    raw_bytes = await file.read()
    csv_reader = _read_upload_as_csv(raw_bytes)

    try:
        resources = aggregate_resource_costs(csv_reader)
    except KeyError as exc:
        raise HTTPException(
            status_code=400,
            detail=f"CSV is missing an expected column: {exc}",
        )

    if not resources:
        return JSONResponse(
            status_code=400,
            content={"error": "No resources found after applying the included resource group filter."},
        )

    excel_buffer = build_excel_report(resources)
    filename = f"consolidated_cost_report_{date.today().isoformat()}.xlsx"

    return StreamingResponse(
        excel_buffer,
        media_type=EXCEL_MEDIA_TYPE,
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )

