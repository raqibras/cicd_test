from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import csv
from io import StringIO


app = FastAPI()

from parse_cost import cost_per_application
@app.post("/parse_cost")
async def parse_cost(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        csv_reader = csv.DictReader(StringIO(contents.decode("utf-8")))

        return cost_per_application(csv_reader)

    except Exception as e:
        return {"error": f"Failed to read CSV file: {str(e)}"}