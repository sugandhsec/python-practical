import json
# import jsonString
import re
from camelcase import camel
# Opening JSON file
f = open('j1.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
str1 = json.dumps(data);

for i in data:
    for j in data[i]:
       a=camel(j)  
       str1.replace(j,a)
       data = json.loads(str1);
f.close()