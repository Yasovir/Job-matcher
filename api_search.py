import requests
from api_information import app_id,app_key
url=f"https://api.adzuna.com/v1/api/jobs/at/search/1?app_id={app_id}&app_key={app_key}"
info=requests.get(url)
data=info.json()
jobs=data["results"]


    

def translate_job(job):
    data_company=job.get("company",{})
    company=data_company.get("display_name","unknown")
    return {"title":job["title"],"company":company ,"id":job["id"],"url":job["redirect_url"]}
    

clean_jobs=[]
for job in jobs:
    clean=translate_job(job)
    clean_jobs.append(clean)
print(clean_jobs)

