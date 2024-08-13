#!/usr/bin/python3
"""
Module with method
"""
import requests


def top_ten(subreddit):
    """Method prints titles of best 10"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }

    params = {
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
