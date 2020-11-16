import json

def getdata():
    with open('df.json') as f:
        data = json.load(f)
    return data
