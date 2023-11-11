import os, json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

dataFolder = 'testCase_data'
jsonPath = os.path.join(dataFolder, 'data.json')

with open(jsonPath, 'r') as file:
    data = json.load(file)

jsonTexts, jsonTitles = [], []
for slideData in data:
    textBoxes = slideData['text']
    slideText = ' '.join(textBoxes)
    jsonTexts.append(slideText)
    jsonTitles.append(textBoxes[0])

datasetPath = os.path.join(os.getcwd(), 'dataset')
allTexts = [] 
categories = []
for category in os.listdir(datasetPath):
    categoryPath = os.path.join(datasetPath, category)
    if os.path.isdir(categoryPath):
        for filename in os.listdir(categoryPath):
            if filename.endswith('.txt'):
                filePath = os.path.join(categoryPath, filename)
                with open(filePath, 'r') as file:
                    text = file.read()
                    allTexts.append(text)
                    categories.append(category)

allTexts.extend(jsonTexts)
categories.extend(jsonTitles)

vectorizer = TfidfVectorizer()
texts_train = vectorizer.fit_transform(allTexts)

model = MultinomialNB()
model.fit(texts_train, categories)

# Use .transform(jsonTexts) to do all slides, and .transform([' '.join(jsonTexts)]) to do the slideshow as a whole
# listToPredict = vectorizer.transform(jsonTexts)
listToPredict = vectorizer.transform([' '.join(jsonTexts)])
prediction = model.predict(listToPredict)[0]

print(f'Predicted category for the JSON text: {prediction}')
