#!/usr/bin/python3
"""
returns number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    headers = {"User-Agent": "Custom"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False).json()
    try:
        return r["data"]["subscribers"]
    except KeyError:
        return 0
