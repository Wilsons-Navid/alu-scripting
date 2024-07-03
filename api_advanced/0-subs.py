#!/usr/bin/python3
"""
Python script that returns the number of subscribers
    for a given subreddit
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit=subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0


if __name__ == "__main__":
    subreddit = argv[1]
    print(number_of_subscribers(subreddit))
