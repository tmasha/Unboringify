from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os, json

dataFolder = 'testCase_data'
filePath = os.path.join(dataFolder, 'data.json')

if os.path.exists(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
else:
    exit(0)

'''
tfidf = TfidfVectorizer()
x = tfidf.fit_transform(slides)

model = MultinomialNB()
model.fit(x_train, y_train)
'''
