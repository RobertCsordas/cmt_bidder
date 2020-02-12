#!/usr/bin/env python3

with open("votes.txt") as v:
    votes = v.read()

votes=[v.strip() for v in votes.split(",")]

eager = set([int(v[:-1].strip()) for v in votes if v.endswith("*")])
rest = set([v2 for v2 in [int(v.strip()) for v in votes if not v.endswith("*")] if v2 not in eager])

print(f"Total number of papers: {len(eager) + len(rest)}")

print(f"eager = {list(eager)};")
print(f"rest = {list(rest)};")
