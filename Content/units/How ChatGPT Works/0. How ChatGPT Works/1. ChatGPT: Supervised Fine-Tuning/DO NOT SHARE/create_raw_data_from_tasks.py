# %%
import json
from pprint import pprint
from glob import glob

task_files = glob('tasks*.json')
print("Collating task files:", task_files)

tasks = []
for idx, fn in enumerate(task_files):
    with open(fn) as f:
        data = json.load(f)

    tasks.extend([
        {
            "prompt": task["params"]["attachments"][0]["content"],
            "response": task["response"]["annotations"]["response"],
        }
        for task in data if "response" in task
    ])
pprint(tasks)

with open(f'raw_data.json', 'w') as f:
    json.dump(tasks, f, indent=4)
    # %%
