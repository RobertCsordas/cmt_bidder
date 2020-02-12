#!/usr/bin/env python3

import requests
import merge
import json

with open("config.json") as f:
    config = json.load(f)

NotEntered = 1
Eager = 5
Willing = 4
InAPitch = 3
NotWilling = 2

URL="https://cmt3.research.microsoft.com/api/odata/"+config["conference"]+"/BiddingModels(%d)"

def bid(paper_id, bid_type):
    url = URL % paper_id
    print(url)
    r = requests.patch(url, '{"BidId": '+str(bid_type)+"}",
    headers={
        'prefer': 'return=representation', 
        'Content-Type': 'application/json',
        'cookie': config["cookie"]
    })
    new_type = int(r.json()["BidId"])
    if new_type!=bid_type:
        print(f"Failed to set bid ID for paper {paper_id} to {bid_type}. It is still {new_type}")

for id in merge.eager:
    bid(id, Eager)

for id in merge.rest:
    bid(id, Willing)