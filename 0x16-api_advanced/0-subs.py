#!/usr/bin/python3
"""
module with a function that queries the Reddit API
and returns the number of subscribers
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=headers)
    all_data = response.json()

    try:
        return all_data.get('data').get('subscribers')
    except Exception as e:
        return 0
