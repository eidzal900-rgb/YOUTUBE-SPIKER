import json

OUTPUT = "data/scripts.json"

def generate_scripts():

    with open("data/spikes.json") as f:
        spikes = json.load(f)

    scripts = []

    for v in spikes[:10]:

        script = {
            "title": v["title"],
            "script": f"""
Hook:
Did you know this about {v['title']}?

Main:
This video is exploding on YouTube.

Outro:
Follow for more crazy discoveries.
""",
            "variations":[
                "You won't believe this",
                "This video shocked everyone"
            ]
        }

        scripts.append(script)

    with open(OUTPUT,"w") as f:
        json.dump(scripts,f,indent=2)

    return scripts
