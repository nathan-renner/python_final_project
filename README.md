# WebScraping and Job Matching Application

### By Nathan Renner

This goal of this project is to webscrape job postings in order to match a candidate's resume with the posting that has the most similarities. To do this, the requests and BeautifulSoup4 modules were used for webscraping, and nltk.corpus's stopwords were used to help eliminate any unnecessary words from both the candidate's resume as well as the job descriptions. Using logic, loops, and if statements, a score comparing the number of similar words between a resume and job description is formed, and the output is an array of job postings ranked by their score.

### A few notes:

- Split the project into a few modules for better organization.
- Since Indeed loads an iframe for each embeded job description search result, I looped through and requested more data to load the individual job ad page. When this loaded, I was able to get the full job description.
- Also, like most games, the highest score wins!
