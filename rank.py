from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

# convert file to one big list of unique words
def convertFile(file):
    wordList = []
    for line in file:
        wordList += convertString(line)
    # remove duplicates from list
    newList = []
    [newList.append(x) for x in wordList if x not in newList]
    return newList

# convert string to list of unique words
def convertString(desc):
    wordList = []
    for word in desc.split():
        word = word.lower()
        if word[-1] == ".":
            word = word[:-1]
        if word not in stopwords and not word.isnumeric() and word not in wordList:
            wordList.append(word)
    return wordList

# compare two arrays and returns new array with similar words
def compare(arr1, arr2):
    compareList = []
    for word in arr1:
        if word in arr2:
            compareList.append(word)
    return compareList

# returns list of jobs and their scores of how many similar words with resume
def getScores(resume, jobs):
    resume = convertFile(resume)
    for job in jobs:
        score = len(compare(resume, job["wordlist"]))
        job["score"] = score;
    jobs.sort(key = lambda job: job["score"], reverse = True)
    return jobs