import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library

def test_add_student_data():
    url = "http://thetestingworldapi.com/api/studentsDetails" # API url
    file = open('E:\Automation\Pytest-API\StudentData.json') # json of the API
    json_request = json.loads(file.read()) # reading json

    object = Library.Common("E:\Automation\Pytest-API\Students.xlsx", "Sheet1") # Taken from Library Class
    column = object.fetch_columns_count()
    rows = object.fetch_row_count()
    keyList = object.fetch_key_names()

    for i in range(2, rows+1):
        updated_json_request = object.update_request_with_data(i, json_request, keyList)
        response = requests.post(url, updated_json_request)
        print(response)

