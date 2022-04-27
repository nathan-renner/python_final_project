from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

resume = open("resume.txt", "r");

dictionary = {}

for line in resume:
    for word in line.split():
        word = word.lower()
        if word[-1] == ".":
            word = word[:-1]
        if word not in stopwords:
            if dictionary.get(word) == None:
                dictionary[word] = 1
                print(word)
            else:
                dictionary[word] = dictionary[word] + 1

print(dictionary)