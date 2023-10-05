import json

with open('sample.json', 'r') as json_file:
    x = json.load(json_file)


print("Courses:", x['courses'])