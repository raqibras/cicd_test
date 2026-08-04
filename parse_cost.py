from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import csv
from io import StringIO
from config import RESOURCE_GROUP_TO_PROJECT_MAPPING, INCLUDED_RESOURCE_GROUPS, RESOURCE_TO_PROJECT_MAPPING



def cost_per_application(csv_reader: csv.DictReader) -> dict:

    project_costs = {}

    for row in csv_reader:
        resource_group = row.get("ResourceGroupName")
        resource_name = row.get("Resource")

        #Check if the resource group is in the included list
        if resource_group not in INCLUDED_RESOURCE_GROUPS:
            print(f"Resource group {resource_group} is not in the included list. Skipping.")
            continue
        
        if resource_name in RESOURCE_TO_PROJECT_MAPPING:
            project_name = RESOURCE_TO_PROJECT_MAPPING[resource_name]
            print(f"Resource {resource_name} maps to project {project_name}.")
            if project_name in project_costs:
                project_costs[project_name] += float(str(row['Cost']))
            else:
                project_costs[project_name] = float(str(row['Cost']))

        #Check if resource group to project mapping exists
        elif resource_group in RESOURCE_GROUP_TO_PROJECT_MAPPING:
            project_name = RESOURCE_GROUP_TO_PROJECT_MAPPING[resource_group]
            print(f"Resource group {resource_group} maps to project {project_name}.")
            if project_name in project_costs:
                project_costs[project_name] += float(row.get("Cost", 0))
            else:
                project_costs[project_name] = float(row.get("Cost", 0))

        else:
            # If no mapping exists, you can choose to log it or handle it as needed
            print(f"No mapping found for resource group {resource_group} or resource {resource_name}. Skipping.")
            continue

    return project_costs

