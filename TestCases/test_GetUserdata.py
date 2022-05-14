import requests
import json
import jsonpath


def test_fetch_user_details():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    json_response = json.loads(response.text)
    qtyOfData = len(json_response['data'])
    for i in range(qtyOfData):
        firstName = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
        print(*firstName)
