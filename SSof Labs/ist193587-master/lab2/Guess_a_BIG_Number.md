# ist193587

## Vulnerabilty

Endpoint is vulnerable to brute-force attack

## Where

Situated at http://mustard.stt.rnl.tecnico.ulisboa.pt:22052/guess/number

## Impact

Allows to find the server's guess by enumeration

## Steps to Reproduce

1. Run the file 'Guess_a_BIG_Number.py' 
2. This file what it does is saves the cookie of the session and guesses a number, but instead of doing it randomly guesses it by halves since the server says it is higher or lower than the guess that was made. If it is higher the min_value will be the guess that was made, if it is lower the max_value is the one that changes. With this it just takes some tries till it figures out the correct number.