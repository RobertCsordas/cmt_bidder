# Microsoft CMT paper bidding tool

## What is it good for?

If you want to distribute the paper reviews in your team, you also might want people from the team to bid for the papers. But bidding requires to be logged in with your account.

This tool enables to download the list of titles and abstracts, send that to people, collect their responses and upload the bids automatically.

## How to use it?

1) Log in to the CMT site. Extract cookie from the browser debug console (needed for the session). You can do this by inspecting the header of any request, and copying the cookie line from there.
2) Create 'config.json' with cookie and conference name (see template below)
3) Run download.py. This will create filtered.json with the raw data and output.txt which is a more human readable format with paper ordered by their relevance score. Send this to your collegues.
4) Collect the votes of your collegues in a format of comma delimited ID lists, with stars after the "Eager" votes. The rest of them will be "Willing". An example list looks like "34,56*,1235*,64"
5) Paste all the ID lists in votes.txt (you can use spaces and newlines after commas)
6) Optional: If you want to check how many votes are there and which papers are eagers and which willing, run "merge.py"
7) Run bid.py

## Example "config.json"

```json
{
    "conference": "ICML2020",
    "cookie": ".AspNet.Cookies=some_ver_long_id; .TRACK=1; .ROLE=Reviewer"
}
```

## Example "votes.txt"

```
294*,432*,3901,5477*,5593*,6986,
124*,589*,968*,136,3897,
```