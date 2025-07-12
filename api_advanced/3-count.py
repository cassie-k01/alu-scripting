#!/usr/bin/python3
"""
Count and print keyword occurrences in hot post titles of a subreddit.
"""

import requests


def count_words(subreddit, word_list, after="", counts={}):
    """Recursive keyword counter for hot post titles."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'SimpleBot/1.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    after = data.get("after")
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0) + title.count(w)

    if after:
        return count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(
        [(w, c) for w, c in counts.items() if c > 0],
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_counts:
        print(f"{word}: {count}")
