#!/usr/bin/python3
"""
get title of the hottest 10 posts of a subreddit.
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(
        url,
        headers={"User-Agent": "Custom"},
        allow_redirects=False,
        params={"limit": 10}).json()
    try:
        for item in r["data"]["children"]:
            print(item["data"]["title"])
    except KeyError:
        print("None")
