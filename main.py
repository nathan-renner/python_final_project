# Author: Nathan Renner

import scrape
import rank

if __name__ == "__main__":
    # Searching for "React Developer" positions around Hoboken, NJ
    searchUrl = "https://www.indeed.com/jobs?q=react%20developer&l=Hoboken%2C%20NJ"
    jobUrl = "https://www.indeed.com/viewjob?jk="

    # get job data from scrape module (while loop to re-request if response has no data)
    jobs = []
    while len(jobs) == 0:
        jobs = scrape.getJobs(searchUrl, jobUrl)

    # open resume file
    resume = open("./assets/resume-react.txt", "r")

    # cycle through jobs and parse job descriptions to have list with unique words
    for job in jobs:
        job["wordlist"] = rank.convertString(job["description"])

    # get and rank scores comparing resume to job wordlists
    jobs = rank.getScores(resume, jobs)
    print("\n")
    for job in jobs:
        print("\n------------------------------------------------------------")
        print("Score: ", job["score"])
        print("Job Title: ", job["title"])
        print("Job ID: ", job["id"])
        print("Description: " + job["description"].replace("\n", " ")[0:60] + "...")
