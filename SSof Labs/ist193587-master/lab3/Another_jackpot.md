# ist193587

## Vulnerabilty

Problem of concurrency/lack of proper synchronization

## Where

The window of vulnerability is situated when logging in and getting the jackpot

## Impact

Allows the user to be admin

## Steps to Reproduce

1. Run the file 'Another_jackpot.py' 
2. This file what it does is create 2 threads where one of them does a get on the jackpot and the other tries to login has 'admin', the validation for jackpot only uses the username and if it's admin it let's you in, so the password can be random doesn't really matter. So doing a race with 2 threads can force the username to be admin even if you fail the password letting you get the jackpot.