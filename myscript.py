import csv
import json
import sys
from camelcase import camel
# Function to convert a CSV to JSON
# Takes the file paths as arguments


def make_json(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['line_code']
            data[key] = rows
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


argumentList = sys.argv[1:]
csvFilePath = argumentList[0]
jsonFilePath = argumentList[1]
make_json(csvFilePath, jsonFilePath)

f = open('j1.json')
data = json.load(f)

for i in data:
    str1 = json.dumps(data);    
    for j in data[i]:
       a=camel(j)  
       str1.replace(j,a)
       data = json.loads(str1);
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
f.close()
