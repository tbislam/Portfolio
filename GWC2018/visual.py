import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity = []
subjectivity = []

for tweet in tweetData:
    tweetblob = TextBlob(tweet["text"])
    polarity.append(tweetblob.polarity)
    subjectivity.append(tweetblob.subjectivity)

#polarity = [.5]
print(polarity)
total = sum(polarity)
average = total/len(polarity)
print(average)


plt.hist(polarity, bins=[-1,-.75,-0.5,-.25, 0.0,.25, 0.5, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()

print(subjectivity)
total = sum(subjectivity)
average = total/len(subjectivity)
print(average)
