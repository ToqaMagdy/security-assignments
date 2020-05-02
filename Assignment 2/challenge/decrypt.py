import sys
from struct import pack, unpack


def F(w):
    return ((w * 31337) ^ (w * 1337 >> 16)) % 2 ** 32


def decrypt(block):
    a, b, c, d = unpack("<4I", block)
    for rno in range(32):
        d = d ^ 1337
        x = a
        a = c ^ F(d | F(d) ^ d)
        b = b ^ F(d ^ F(a) ^ (d | a))
        c = x ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a)

        x = a
        a = d ^ 31337
        d = c ^ F(a | F(a) ^ a)
        c = b ^ F(a ^ F(d) ^ (a | d))
        b = x ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d)
    return pack("<4I", a, b, c, d)


pt = open("flag.enc").read()
while len(pt) % 16: pt += "#"

ct = "".join(decrypt(pt[i:i + 16]) for i in range(0, len(pt), 16))

open("output" + ".enc", "w").write(ct)
