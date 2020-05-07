#!/usr/bin/python3
"""
get title of the hottest 10 posts of a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    recurse_helper(subreddit, [])


def recurse_helper(subreddit, hot_list=[], name=""):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(
        url,
        headers={"User-Agent": "Custom"},
        allow_redirects=False,
        params={"after": name}).json()
    try:
        for item in r["data"]["children"]:
            if item["data"]["title"] == []:
                return hot_list
            hot_list.append(item["data"]["title"])
            print("----------------\n{}\n----------------".format(item["data"]["title"]))
    except KeyError:
        return None
    return recurse_helper(subreddit, hot_list, item["data"]["name"])

