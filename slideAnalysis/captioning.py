import os, json
path = os.getcwd() + '/testCase_data/data.json'

with open(path, 'r') as file:
    data = json.load(file)

