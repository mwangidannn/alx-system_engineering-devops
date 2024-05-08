#!/usr/bin/python3

"""
function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
"""

import requests
def number_of_subscribers(subreddit):
    #This is  URL for the Reddit API endpoint to retrieve subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse JSON response to extract number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 302:  # Redirect status code indicating invalid subreddit
        return 0
    else:
        # Handle other possible error cases
        print(f"Error: {response.status_code}, {response.text}")
        return 0
