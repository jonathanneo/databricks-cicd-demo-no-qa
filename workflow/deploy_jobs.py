from databricks import jobs.api.JobsApi
import os 
import json 

all_jobs = JobsApi.list_jobs()

files = os.listdir("jobs")

for file in files: 
    with open(file, "r") as fp: 
        json_content = json.loads(fp)

    file_name = file["name"]
    job_found = False 
    for job in all_jobs: 
        if job == file_name: 
            job_found = True 
    
    if not job_found: 
        JobsApi.create_job(json_content)
