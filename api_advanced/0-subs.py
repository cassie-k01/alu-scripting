#!/usr/bin/python3
"""
Return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers.
    Returns 0 if subreddit is invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "CassieBot/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError, KeyError):
        return 0
