#!/usr/bin/python3
"""
Fetches all hot post titles from a given subreddit using recursion.
"""
import requests

headers = {'User-Agent': 'CassieBot/1.0'}


def recurse(subreddit, after="", hot_list=[], page_counter=0):

    subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)

    parameters = {'limit': 100, 'after': after}
    response = requests.get(subreddit_url, headers=headers, params=parameters)

    if response.status_code == 200:
        json_data = response.json()

        for child in json_data.get('data').get('children'):
            title = child.get('data').get('title')
            hot_list.append(title)

        after = json_data.get('data').get('after')
        if after is not None:

            page_counter += 1
            # print(len(hot_list))
            return recurse(subreddit, after=after,
                           hot_list=hot_list, page_counter=page_counter)
        else:
            return hot_list

    else:
        return None


if __name__ == '__main__':
    print(recurse("recursor"))
