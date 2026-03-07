import random
import json
import os

DATA_FILE = "data/spikes.json"

def detect_spikes():

    spikes = []

    for i in range(20):

        spikes.append({
            "title": f"Viral Video {i}",
            "views": random.randint(10000,200000),
            "score": random.randint(50,100),
            "niche": random.choice([
                "AI Tools",
                "Weird Facts",
                "Apps"
            ])
        })

    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE,"w") as f:
        json.dump(spikes,f,indent=2)

    return spikes
