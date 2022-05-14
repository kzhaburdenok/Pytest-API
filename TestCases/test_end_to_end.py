import requests
import json
import jsonpath

def test_Add_new_data():
    App_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('E:\Automation\Pytest-API\RequestJson.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(App_URL, request_json)

    id = jsonpath.jsonpath(response.json(), 'id')
    print("my id is ", id[0])

    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    file = open('E:\Automation\Pytest-API\TechDetails.json', 'r')
    request_json = json.loads(file.read())  
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]      
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    address_api_url = "http://thetestingworldapi.com/api/addresses"
    file = open('E:\Automation\Pytest-API\AddressJson.json', 'r')
    request_json = json.loads(file.read())    
    request_json['stId'] = id[0]  
    response1 = requests.post(address_api_url, request_json)

    final_details_url = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(final_details_url)
    print(response.text)