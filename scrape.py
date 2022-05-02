import time
import requests
from bs4 import BeautifulSoup

# get text data from request grab
def getData (url):
    return requests.get(url, timeout = 10).text

# parse test to html from request grab
def getHTML (url):
    data = getData(url)
    soup = BeautifulSoup(data, 'html.parser')
    return soup

# filter html to return list of dictionaries with job ids and titles
def getJobIds (soup):
    data = []
    for item in soup.find_all("a", class_="jcs-JobTitle"):
        data.append({ "id":item['data-jk'], "title":item.get_text()})
    return data

# filter job posting page and return job object including job description
def getJobDescriptions (url, jobs):
    for job in jobs:
        soup = getHTML(url + job["id"])
        description = soup.find("div", class_="jobsearch-jobDescriptionText").get_text()
        job["description"] = description
    return jobs

# function to get all job data needed in main.py
def getJobs (url, jobUrl):
    soup = getHTML(url)
    jobData = getJobIds(soup)
    jobData = getJobDescriptions(jobUrl, jobData)
    return jobData