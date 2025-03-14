# ist193587

## Vulnerabilty

Buffer-overflow.

## Where

The ```gets(buffer)``` allows the user to overflow the buffer.

## Impact

Allows the user pass the if statement and with that call another function.

## Steps to Reproduce
1. We know the size of the buffer (10) so we can fill the buffer with a string of size 10.
2. Looking through the gdb we can disassemble main and also disassemble win to check the memory addresses that are allocated, we can do ```x win``` to get the memory address for that function, in this is ```0x080486f1```. We can also run it and see that although the buffer has size 10, the EIP that we are trying to reach (since there is no call to the function we need to use the EIP to go there) is only after 22 bytes. 
3. With this in mind, we can create a simple python script, like Return_Address.py , that allows us to fill the buffer and afterwards insert the memory address for ```win()```, in this case i used ```p32(elf.symbols['win'])``` instead of ```p32(0x080486f1)``` but both work.
