#!/usr/bin/python3
"""
A script that use reddit api to outputs the
number of subscribers of a certain subreddit.
"""


import json
import requests


def number_of_subscribers(subreddit):

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data['data']['subscribers']

    else:
        return 0
