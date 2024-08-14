#!/usr/bin/python3
"""
Module with method
"""

import requests


def top_ten(subreddit):
    """Method for top ten subreddits"""
    # API endpoint URL
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    # GET request to API
    response = requests.get(url, headers=headers)
    
    # request, success or not
    if response.status_code == 200:
        data = response.json()
        
        titles = [post['data']['title'] for post in data['data']['children']]
        
        for title in titles:
            print(title)
    else:
        print(None)

