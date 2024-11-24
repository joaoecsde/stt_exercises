# ist193587

## Vulnerabilty

Buffer-overflow.

## Where

The ```gets(buffer)``` allows the user to overflow the buffer.

## Impact

Allows the user pass the if statement.

## Steps to Reproduce
1. Simply using has an input a string bigger than 128 overflows the system. Don't use a too large string since it may break the system. So something like this: ```111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111```
