import re
import requests
import json
import jsonpath

def test_with_oAuth():
    token_url = "http://thetestingworldapi.com/Token"
    data = {
        'grant_type' : 'password',
        'username': 'admin',
        'password': 'adminpass'
    }
    response_token = requests.post(token_url,data)
    print(response_token.text)

    token_value = jsonpath.jsonpath(response_token.json(), 'access_token')

    auth = {
        'Authorization':'Bearer ' + token_value[0]
    }

    url = "http://thetestingworldapi.com/api/StDetails/1104"
    response = requests.get(url, headers=auth)
    print(response.text)