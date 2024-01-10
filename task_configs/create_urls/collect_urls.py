import pandas as pd
import json

df = pd.read_csv('task_configs/create_urls/eval_links.csv')

urls = df['link'].tolist()

z = []

for u in urls:
    x = {
        "url": u,
        "task_name": "new_platform_evals"
    }
    z.append(x)

with open('task_configs/create_urls/eval_urls.json', 'w') as f:
    json.dump(z, f, indent=2)