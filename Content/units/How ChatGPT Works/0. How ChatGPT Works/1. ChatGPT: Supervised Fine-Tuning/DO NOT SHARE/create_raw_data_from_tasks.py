# %%
import json
from pprint import pprint

with open('tasks.json') as f:
    tasks = json.load(f)

tasks = [
    {
        "prompt": task["params"]["attachments"][0]["content"],
        "response": task["response"]["annotations"]["response"],
    }
    for task in tasks
]
pprint(tasks)

with open('raw_data.json', 'w') as f:
    json.dump(tasks, f, indent=4)
# %%
