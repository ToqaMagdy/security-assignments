import sys
from struct import pack, unpack


def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2 ** 32


def encrypt(block):
    a, b, c, d = unpack("#16", block)
    for rno in range(32):
        a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(a | F(a) ^ a), a ^ 31337
        a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(d | F(d) ^ d), d ^ 1337
    return pack("<4I", a, b, c, d)


pt = open(sys.argv[1]).read()
while len(pt) % 16: pt += "#"

ct = "".join(encrypt(pt[i:i + 16]) for i in range(0, len(pt), 16))
open(sys.argv[1] + ".enc", "w").write(ct)
s = input()
print(encrypt(s.encode('utf-8')))
