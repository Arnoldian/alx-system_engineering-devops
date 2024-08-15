#!/usr/bin/python3
"""
Module to query the Reddit API for subscriber count.
"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a specific subreddit. If the subreddit is invalid, it returns 0.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: No. of subs or 0 if subreddit is invalid.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
