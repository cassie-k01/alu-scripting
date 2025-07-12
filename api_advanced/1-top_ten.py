#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the top ten post titles of a given subreddit"""
    headers = {'User-Agent': 'CassieBot/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/.json"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts[:10]:
            print(post.get('data', {}).get('title'))
    else:
        print(None)
