from pwn import *

logging.getLogger("pwnlib").setLevel(logging.ERROR)

p = remote('titan.picoctf.net',55084)

p.recvuntil(b'flag.\n')

word = (p.readline().split(b': ')[-1].replace(b'\n',b'')).decode('utf-8')

a = word.encode('utf-8').hex()[::-1]

hexword = ''.join([a[i+1] + a[i] for i in range(0, len(a)-1, 2)])

p.sendlineafter(b'representation: ',hexword.encode('utf-8'))

p.readline()

p.sendlineafter(b'representation: ', word.encode('utf-8').hex().encode('utf-8'))

p.readline()

print(p.read().split(b' ')[-1].replace(b'\n\n',b'').decode('utf-8'))