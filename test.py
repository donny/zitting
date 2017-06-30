import json
from hackernews import HackerNews

hn = HackerNews()
results = []

for story_id in hn.top_stories(limit=10):
    results.append(hn.get_item(story_id).title)

print(json.dumps(results))
