#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://api.reddit.com/r/{subreddit}/hot?limit=10"
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data')
    if not data or 'children' not in data:
        print(None)
        return

    for post in data.get('children'):
        print(post.get('data').get('title'))
