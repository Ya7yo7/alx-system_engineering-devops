#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API
and returns a list of all hot article titles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If the subreddit is invalid,
    returns None.
    """
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    headers = {'User-Agent': 'CustomClient/1.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if not data or 'children' not in data:
        return None

    for post in data['children']:
        hot_list.append(post['data']['title'])

    if data.get('after') is not None:
        return recurse(subreddit, hot_list, data['after'])

    return hot_list
