# ist193587

## Vulnerabilty

Buffer-overflow.

## Where

The difference between password size and buffer size, and making a ```strcpy()``` of them.

## Impact

Allows the user pass the if statement.

## Steps to Reproduce
1. We know the size of the buffer (32) and the password size (64).
2. Looking through the gdb we can disassemble main and also disassemble check_password to check the memory addresses that are allocated. Making a normal run we can check the memory addresses for EBX, EBP and EIP we need to know those since we need to go back to main from check_passwords and if the EBX value is random we may not go back to main so the value should be ```0x0804a000```, the EBP value is not really important in this case so it can be random, EIP value will be the memory address that refers to the call of ```getflag()``` so it should be ```0x080487d9```.
3. With this in mind, we can create a simple python script, like Super_Secure.py , that allows us to fill the buffer and afterwards insert EBX value then EBP and finally EIP. This script will work fine but if you use the value of EBX ```0x0804a000``` it will fail, because the ```strcpy()``` function in c will read till a ```\0``` and EBX will have a \0 in it not copying the rest of the line, to escape this we can advance 1 byte, this will make the printf start in the second byte instead of the first but this will not be a problem in this case.
