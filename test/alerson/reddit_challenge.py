import json
import requests

def get_controversial(limit):
    result = []
    r = requests.get('http://api.reddit.com/new?limit=%s' % (limit))
    if r.status_code == 200:
        reddit_data = r.json()
        score = 0
        for link in reddit_data['data']['children']:
            #result.append((link['data']['ups'], link['data']['downs'], link['data']['title'], link['data']['url']))
            score_final = link['data']['ups'] - link['data']['downs']*200
            if 
            
    return result
print(get_controversial(20))