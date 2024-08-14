#!/usr/bin/python3
"""
Module using method
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Method returning hot list"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 404:
        return None

    data = response.json()

    if 'data' not in data or len(data['data']['children']) == 0:
        return hot_list if hot_list else None

    for post in data['data']['children']:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list

