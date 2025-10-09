import random
import requests
import json
form_params = {'Name': 'Wilson', 'Grades[]' : [1,2,3]}

response = requests.post('https://thor.cnt.sast.ca/~demo/cmpe2000/ica10_jsonResponse.php', data=form_params)
print(response.status_code)
if response.status_code == requests.codes.ok:
    stuff = response.json()
    print(stuff)

grades = [random.randint(1, 100) for _ in range(1,20)]
form_params = {'Name': 'Wilson', 'Grades[]' : grades}
response = requests.post('https://thor.cnt.sast.ca/~demo/cmpe2000/ica10_jsonResponse.php', data=form_params)
if response.status_code == requests.codes.ok:
    stuff = response.json()
    print(stuff)