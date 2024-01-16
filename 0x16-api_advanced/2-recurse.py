#!/usr/bin/python3
"""Function to query a list of all hot posts on a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/dblay112_)"
        }
    param = {
            "after": after,
            "count": count,
            "limit": 100
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        results = data['data']['children']
        if not results:
            return hot_list

    title = [results['data']['title'] for r in results]
    hotlist.extend(title)

    after = data['data']['after']
    return recurse(subreddit, hot_list, after)
    else:
        return None
