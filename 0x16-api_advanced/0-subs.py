#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        results = requests.get(url, allow_redirects=False,
                           headers={'User-Agent': 'MyChromeBook'})
        return results.json().get('data').get('subscribers')
    except Exception:
        return 0
