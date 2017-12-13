

import requests
from bs4 import BeautifulSoup

#just a data store for the IDs 
job_ids = dict([
        (27,'real estate (license OR agent)'),
        (23,'"Inside Sales"  OR Telemarketer OR ("Customer Service" AND Sales)'),
        (24,'"Sales Manager" OR "Sales Director"')
    ])

#get job based on ID
def job_string(id):
    return job_ids[id];

def create_url(resume_query,location):
    indeed_string = "https://www.indeed.com/resumes"+"?co=US&q="+ resume_query +"&l="+location+"&lmd=month"
    return indeed_string

#requests 
def get_num_resumes(id,location):
    page = requests.get(create_url(job_string(id),location))

    contents = page.content

    soup = BeautifulSoup(contents, "html.parser")

    numjobs_sample = soup.find('div',attrs={'id':'result_count'})

    num = ''.join(c for c in numjobs_sample.text if c.isdigit())

    return num
    