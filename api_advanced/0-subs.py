#!/usr/bin/python3
"""DOCS-1"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Mozilla/5.0 (compatible; Bot/1.0)'}

    try:
        response = requests.get(reddit_url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0
