import requests as re


def extract_api(url):
    """extract an api call and return it as a dictionary"""
    try:
        response = re.get(url)

    except Exception as e:
        print("Can't connect to the API: ", e)

    if response.status_code == 200:
        return response.json()
    else:
        print("Can't extract the information")