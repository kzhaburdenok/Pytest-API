import py
import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"

@pytest.fixture
def start_exec(scope="module"):
    global file # it will make file global - used everywhere
    file = open('UserData.json', 'r')

#@pytest.mark.skip
def test_Create_New_User(start_exec):
    json_input = file.read()
    request_body = json.loads(json_input)
    response = requests.post(url, request_body)
    assert response.status_code == 201, f"Response code is {response.status_code}, but 201 is expected"

def test_Create_Other_User(start_exec):
    json_input = file.read()
    request_body = json.loads(json_input)
    response = requests.post(url, request_body)
    response_json = json.loads(response.text)
    idValue = jsonpath.jsonpath(response_json, 'id')
    print("ID value is", idValue[0])