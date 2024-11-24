# ist193587

## Vulnerabilty

Buffer-overflow and bad use of canaries.

## Where

The difference between guess size and lottery size and ```memcpy()``` function

## Impact

Allows the user pass the if statement.

## Steps to Reproduce
1. We know the size guess (64) and the lottery size (8).
2. Although there is canaries they only work in the existence of a return() so if there is no return we can just overflow with `A`*64 and we pass the if statement.
