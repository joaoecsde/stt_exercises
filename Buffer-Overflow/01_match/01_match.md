# ist193587

## Vulnerabilty

Buffer-overflow.

## Where

The ```gets(buffer)``` allows the user to overflow the buffer.

## Impact

Allows the user pass the if statement.

## Steps to Reproduce
1. We know what we need to bypass the if statement just have the variable test match ```0x61626364``` to do this we can fill the buffer with a random string with a size of 64 and afterwards insert the charactes that represent the hexadecimal ```61 = a , 62 = b , 63 = c , 64 = d```.
2. It will not pass the test still because it is actually inverted so it should look something like this:
```1111111111111111111111111111111111111111111111111111111111111111dcba```