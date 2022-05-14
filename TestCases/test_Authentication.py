import requests
from requests.auth import HTTPBasicAuth

def test_with_auth():
    response = requests.get('https://api.github.com/user', auth = HTTPBasicAuth('kzhaburdenok', '12125896Zx'))
    print(response.text)