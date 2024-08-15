#!/usr/bin/python3
"""
Module to query the Reddit API for hot article titles recursively.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieves the titles of hot articles from a subreddit.

    Args:
        subreddit (str): name of the subreddit.
        hot_list (list): list to accumulate hot article titles.
        after (str): parameter for pagination

    Returns:
        list: list of titles of hot articles or None if subreddit invalid
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    if results is None:
        return None

    after = results.get("after")
    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list

