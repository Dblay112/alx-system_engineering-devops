#!/usr/bin/python3
"""
 a function that queries the Reddit API and prints the titles of the
 first 10 hot posts listed for a given subreddit
 """
 import requests


 def top_ten(subreddit):
     """a query the Reddit API and prints the titles
     of the first 10 hot posts listed for a given subreddit.
     """
     url = "https://www.reddit.com/r/{subreddit}/hot.json"
     headers = {
             "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/dblay112_)"
             }
     response = requests.get(url, headers=headers, params={'limit: 10'}, allow_redirects=False)
     if response.status_code == 200:
         data = response.json()
         results = data["data"]["children"]

         for r in results:
             print(r['data']['title'])
    else:
        print('None')
