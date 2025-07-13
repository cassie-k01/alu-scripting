#!/usr/bin/python3
""" Get the titles of the first 10 hot posts from a subreddit."""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'CassieBot/1.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=True)
    print("Status: {}".format(response.status_code))

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        for post in posts[:10]:
            print(post.get('data', {}).get('title'))
    else:
        print(None)
