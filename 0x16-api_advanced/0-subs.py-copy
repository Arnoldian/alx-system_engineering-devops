#!/usr/bin/python3
"""
Module with method
"""

import requests


def number_of_subscribers(subreddit):
    """Method for number of subscribers for specific subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)

    return subs
