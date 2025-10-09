import requests

#params = "name=Willy&word=Wonky"
form_params = {'name':'Great Gazoo', 'show': 'The Flintstones', 'number': 42}
response = requests.get(f"https://thor.cnt.sast.ca/~demo/cmpe2000/ica10_formtest.php",
                        params=form_params)
print(response.request.url)
print(response.status_code)
if response.status_code == requests.codes.ok:
    print(response.text)

#post time
lab3params = {'tagId': 'all'}
response = requests.post('https://thor.cnt.sast.ca/~demo/cmpe2000/lab03_webservice.php', data=lab3params)
print(response.request.url)
print(response.status_code)
if response.status_code == requests.codes.ok:
    print(response.text)
    stuff = response.json()
    print(type(stuff))
    print(stuff)
    for row in stuff['data']:
        if int(row['tagId']) < 5 or int(row['tagId']) > 195:
            print(f"{row['tagId']}:{row['tagDescription']}")

