#!/usr/bin/python3
"""
get title of the hottest 10 posts of a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], name=""):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(
        url,
        headers={"User-Agent": "Custom"},
        allow_redirects=False,
        params={"after": name}).json()
    try:
        if r["data"]["children"] == []:
            return hot_list
        for item in r["data"]["children"]:
            hot_list.append(item["data"]["title"])
    except KeyError:
        return None
    return recurse(subreddit, hot_list, item["data"]["name"])
