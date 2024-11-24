from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 22055

### run a remote process
s = remote(SERVER, PORT, timeout=9999)

Finish = bytes('FINISH', 'utf-8')
More = bytes('MORE', 'utf-8')
end_of_line = bytes('FINISH)?\n', 'utf-8')

s.recvline()
line_target = s.recvline()
print(line_target)
target = int(line_target.decode('utf-8').split('you get to ')[1].split('.')[0])
print(target)
number = 0
"""s.recvline()
s.recvline()
s.recvline()
s.recvline()
s.recvline()"""

s.recvuntil(end_of_line)

while number != target:
    print(number)
    s.sendline(More)
    current = s.recvline()
    print(current)
    number = int(current.decode('utf-8').split('have: ')[1]) + number
    print(target)
    """s.recvline()
    s.recvline()
    s.recvline()
    s.recvline()
    s.recvline()"""
    s.recvuntil(end_of_line)
    
s.sendline(Finish)
print(s.recvline())

#s.interactive()