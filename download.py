#!/usr/bin/env python3

import requests
import json

with open("config.json") as f:
    config = json.load(f)

URL='https://cmt3.research.microsoft.com/api/odata/'+config["conference"]+'/$batch'

r = requests.patch(URL, '{"requests":[{"url":"/api/odata/'+config["conference"]+'/BiddingModels?&$orderby=Id asc","method":"GET","headers":{"Accept":"application/json"}}]}',
    headers={
     'Content-Type': 'application/json',
     'cookie': config["cookie"]
    }
)

data = r.text
start = data.find("{")
end = data.rfind("}")

data = json.loads(data[start:end+1])

data = data["value"]

keys = ['Id', 'Abstract', 'Title', 'PrimarySubject', 'SecondarySubject', 'Relevance', 'TpmsRank']
data = [{k2: v[k2] for k2 in keys } for v in data]

with open('filtered.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

data.sort(key=lambda x: x["TpmsRank"] or 9999999, reverse=False)

with open('output.txt', 'w') as f:
    for x in data:
        f.write("------------------------------------------------------------------\n")
        f.write(str(x["Id"])+": "+x["Title"]+" ["+x["PrimarySubject"]+"]\n")
        # f.write(x["PrimarySubject"]+"\n")
        f.write("\n"),
        f.write(x["Abstract"].replace("\r\n"," ").replace("\n"," ").replace("  "," ")+"\n"),
        f.write("\n")

