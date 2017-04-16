import json

with open('data.json', 'r') as f:
    data = int(json.load(f))

data += 1

with open('data.json', 'w') as f:
    json.dump(data, f)