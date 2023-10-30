import requests
import json

cx = "CX_ID"
api_key = "GOOGLE_API_KEY"


def search(keyword):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': keyword,
        'cx': cx,
        'key': api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()
    # print(data)
    return data['items'][0]['link']


# Replace with your own Programmable Search Engine ID and API Key

