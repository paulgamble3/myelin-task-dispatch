import pandas as pd
import json

df = pd.read_csv('task_configs/create_urls/eval_links_all_engine_mentoring.csv')

urls = df['link'].tolist()

z = []

for u in urls:
    x = {
        "url": u,
        "task_name": "new_platform_evals"
    }
    z.append(x)

with open('task_configs/create_urls/eval_urls_all_engine.json', 'w') as f:
    json.dump(z, f, indent=2)