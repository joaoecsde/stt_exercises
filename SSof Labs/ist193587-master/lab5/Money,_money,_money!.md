# ist193587

## Vulnerabilty

Endpoint is vulnerable to SQL injection

## Where

Situated in the bio

## Impact

Allows the user to change a readonly variable, in this case to get a jackpot

## Steps to Reproduce

1. First i discovered with this payload in the login `'` some variables that the user has. And I saw one that caught my that's `jackpot_val`
2. With this in mind i created an account, random username and some easy password. after it i went directly to check my profile and there we can see how many tokens we have left.
3. After it i did some testng in the bio since is the only thing that can be written. I did some random payload `' asda '` and we can see that it is injectable. Looking at the error i tried to do this payload `', jackpot_val = '0` and i was able to change the the random number to 0 and this way get the jackpot.