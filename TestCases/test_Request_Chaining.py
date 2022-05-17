from urllib import response
import requests
import json
import jsonpath

def test_add_new_student():
    global id
    url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('E:\Automation\Pytest-API\Files\StudentData.json', 'r')
    json_request = json.loads(file.read())

    response = requests.post(url, json_request)
 
    id = jsonpath.jsonpath(response.json(), 'id')
    print("my id is ", id[0])

def test_get_details():
    url = "http://thetestingworldapi.com/api/studentsDetails/" + str(id[0])
    response = requests.get(url)
    print(response.text)
