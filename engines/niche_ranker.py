import json
from collections import defaultdict

def rank_niches():

    with open("data/spikes.json") as f:
        spikes = json.load(f)

    niches = defaultdict(list)

    for v in spikes:

        niches[v["niche"]].append({
            "title": v["title"],
            "score": v["score"]
        })

    with open("data/niches.json","w") as f:
        json.dump(niches,f,indent=2)

    return niches
