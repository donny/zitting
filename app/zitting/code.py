import json
from hackernews import HackerNews

def handler(event, context):
    hn = HackerNews()
    user = hn.get_user('pg')
    return user.karma
