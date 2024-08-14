#!/usr/bin/python3
"""
Module using method
"""

import requests


def number_of_subscribers(subreddit):
    """Method for subs no."""
    headers = {"User-Agent": "0x16. API_advanced-e_kiminza"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # subreddit valid or not
    if response.status_code != 200:
        return 0
    
    # Parse JSON response, get number of subs
    sub = response.json().get("data", {}).get("subscribers", 0)

    return sub

