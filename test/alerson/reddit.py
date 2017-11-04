import json
import requests
r = requests.get('http://api.reddit.com/controversial?limit=5')
if r.status_code == 200 :
  reddit_data = r.json()
    
print(r.status_code)
print(r)
print(type(r))

for link in reddit_data['data']['children']:
        print("%s/%s - %s - %s" % (link['data']['ups'], link['data']['downs'], link['data']['title'], link['data']['url']))

