import requests
import json
import jsonpath

def test_add_student_data():
    url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('E:\Automation\Pytest-API\StudentData.json', 'r')
    json_request = json.loads(file.read())

    response = requests.post(url,json_request)
    print('\nwe added a student with these data', response.text)

def test_get_student_data():
    url = "http://thetestingworldapi.com/api/studentsDetails/1200718"
    response = requests.get(url)
    #json_response = json.loads(response.text)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response, 'data.id')
    print('\nid is', id)
    assert id[0] == 1200718, f"ID 1200699 is expected, but {id[0]} is displayed"

def test_update_Student_data():
    url = "http://thetestingworldapi.com/api/studentsDetails/1200718"
    file = open('E:\Automation\Pytest-API\StudentDataUpdating.json', 'r')
    json_request = json.loads(file.read())
    response = requests.put(url,json_request)
    print('\nUpdated student status', response.text)   

def test_get_Student_data():
    url = "http://thetestingworldapi.com/api/studentsDetails/1200718"
    response = requests.get(url)
    #json_response = json.loads(response.text)
    json_response = response.json()
    print('\nupdated info is ', json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 1200718, f"ID 1200699 is expected, but {id[0]} is displayed"

def test_delete_student_data():
    url = "http://thetestingworldapi.com/api/studentsDetails/1200719"
    response = requests.delete(url)
    print("\ndeleted user status",response.text)
    
def test_get_Student_data(): 
    url = "http://thetestingworldapi.com/api/studentsDetails/1200719"
    response = requests.get(url)    
    json_response = response.json()
    print("\nuser info", json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print("\nid is ", id[0])
    assert id[0] == 1200719, f"ID 1200719 is expected, but {id[0]} is displayed"