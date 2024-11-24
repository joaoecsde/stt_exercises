# ist193587

## Vulnerabilty

Endpoint is vulnerable to brute-force attack

## Where

Situated at http://mustard.stt.rnl.tecnico.ulisboa.pt:22053/more

## Impact

Allows to get the server's guess by multiple tries

## Steps to Reproduce

1. Run the file 'Python_requests.py' 
2. This file what it does is saves the cookie of the session, and afterwards from the get that is made to the site 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22053/hello' we receive a string and splitting it in order to get the target number. With this we do a while cycle that does a get from the website 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22053/more' until the current value is the same as the target, when it reaches the same value it does a get to the site 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22053/finish'.