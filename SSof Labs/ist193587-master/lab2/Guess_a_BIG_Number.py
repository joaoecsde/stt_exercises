import requests

session = requests.Session()
site = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22052'
response = session.get(site)
cookie = session.cookies.get_dict()

max_value = 100000
min_value = 0

while True:
    guess = int((max_value-min_value)/2)+min_value
    print(guess)
    x = requests.get(site + "/number/" + str(guess), cookies = cookie).text
    print(x)
    if (x == "<h1>Higher!</h1>"):
        min_value = guess
    elif (x == "<h1>Lower!</h1>"):
        max_value = guess 
    else:
        break


