# ist193587

## Vulnerabilty

Buffer-overflow.

## Where

The ```gets(buffer)``` allows the user to overflow the buffer.

## Impact

Allows the user pass the if statement and with that call another function.

## Steps to Reproduce
1. We know the size of the buffer (32) so we can fill the buffer with a string of size 32.
2. Looking through the gdb we can disassemble main and also disassemble win to check the memory addresses that are allocated, we can do ```x win``` to get the memory address for that function, in this is ```0x080486f1```.
3. With this in mind, we can create a simple python script, like Calling_Function.py , that allows us to fill the buffer and afterwards insert the memory address for ```win()```.
