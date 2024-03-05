#!/usr/bin/python3
"""module with a function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
	"""returns the number of subscribers
	for a given subreddit.
	"""
