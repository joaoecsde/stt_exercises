# ist193587

## Vulnerabilty

Endpoint is vulnerable to SQL injection

## Where

Situated in the login

## Impact

Allows the user to login as another user

## Steps to Reproduce

1. First we try to discover which is field is injectable, so i tried a simple injection in the login portion of the website since we have the objective to login as admin. `' OR 1=1; -- '` as the username and a random password and we are able to see it is injectable, and that we even login as admin.
2. I believe that this is not the intended way of solving the exercise so the correct payload to login has admin is `admin'; -- '`