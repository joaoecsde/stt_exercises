# ist193587

## Vulnerabilty

Endpoint is vulnerable to brute-force attack

## Where

Situated at http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/more

## Impact

Allows to get the server's guess by multiple tries

## Steps to Reproduce

1. After looking at the website and and doing some testing we can see 2 things, first is that will be almost impossible to get it in 1 try, and that the cookies that exist are the user value and the remainig_tries value that is set to 1, changing it will allow us to get more than 1 try.
2. Run the file 'Python_requests_Again.py' 
3. This file what it does is saves the cookie of the session, and afterwards from the get that is made to the site 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/hello' we receive a string and splitting it in order to get the target number. We also can set the cookies that we saved in order to get more tries so we change the remaining_tries cookie to have more than enough tries.With this we do a while cycle that does a get from the website 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/more' until the current value is the same as the target, when it reaches the same value it does a get to the site 'http://mustard.stt.rnl.tecnico.ulisboa.pt:22054/finish'.