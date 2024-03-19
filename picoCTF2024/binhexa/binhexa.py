from pwn import *

logging.getLogger("pwnlib").setLevel(logging.ERROR)

p = remote('titan.picoctf.net',58221)

p.recvuntil(b'flag.')

p.readline()

p.readline()

a = p.readline().split(b': ')[-1].replace(b'\n',b'').decode('utf-8')

b = p.readline().split(b': ')[-1].replace(b'\n',b'').decode('utf-8')

print(f"a={a}, b={b}")

operators = [b'>>', b'+', b'|', b'*', b'&', b'<<']

#p.readline()
#p.readline()

for i in range(1,7,1):

	operator = (p.recvuntil(b'Perform').split(b"'")[1])

	print(f"operator: {operator}")

	if operators.index(operator) == 0:
		p.recvuntil(b'by')
		ans = bin(int(b,2) >> 1).encode('utf-8').replace(b'0b',b'')
	if operators.index(operator) == 1:
		ans = bin(int(a,2) + int(b,2)).encode('utf-8').replace(b'0b',b'')
	if operators.index(operator) == 3:
		ans = bin(int(a,2) * int(b,2)).encode('utf-8').replace(b'0b',b'')
	if operators.index(operator) == 2:
		ans = bin(int(a,2) | int(b,2)).encode('utf-8').replace(b'0b',b'')
	if operators.index(operator) == 4:
		ans = bin(int(a,2) & int(b,2)).encode('utf-8').replace(b'0b',b'')
	if operators.index(operator) == 5:
		binary = b if (p.recvuntil(b'by')[-4]) == b'2' else a
		ans = bin(int(binary,2) << 1).encode('utf-8').replace(b'0b',b'')

	p.sendlineafter(b'result: ',ans)

	if i == 6:
		p.sendlineafter(b'hexadecimal: ',hex(int(ans.decode('utf-8'),2)).encode('utf-8').replace(b'0x',b''))
		
print(p.read().split(b' ')[-1].replace(b'\n',b''))
