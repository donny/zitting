import json
from hackernews import HackerNews

def handler(event, context):
    hn = HackerNews()
    results = []
    for story_id in hn.top_stories(limit=10):
        results.append(hn.get_item(story_id).title)

    return json.dumps(results)
