import sys

def shiftEncryption(input, output, key):
    f = open(input, "r")
    s = f.read()
    s2 = ""
    for i in s:
        if i.isalpha() and i.isupper():
            i = chr(((ord(i) - ord('A') + key) % 26)+ord('A'))
            s2+=i
        elif i.isalpha() and i.islower():
            i = chr(((ord(i) - ord('a') + key) % 26) + ord('a'))
            s2+=i
        else:
            s2+=i
        o = open(output, "w")
        o.write(s2)
        o.close()

def shiftDecryption(input, output, key):
    f = open(input, "r")
    s = f.read()
    s2 = ""
    for i in s:
        if i.isalpha() and i.isupper():
            i = chr(((ord(i) - ord('A') - key + 26) % 26)+ord('A'))
            s2+=i
        elif i.isalpha() and i.islower():
            i = chr(((ord(i) - ord('a') - key + 26) % 26) + ord('a'))
            s2+=i
        else:
            s2+=i
        o = open(output, "w")
        o.write(s2)
        o.close()

def affineEncryption(input, output, a, b):
    f = open(input, "r")
    s = f.read()
    s2 = ""

    for i in s:
        if i.isalpha() and i.isupper():
            i = chr(((int(a) * (ord(i) - ord('A')) + int(b)) % 26) + ord('A'))
            s2+=i
        elif i.isalpha() and i.islower():
            i = chr(((int(a) * (ord(i) - ord('a')) + int(b) % 26) + ord('a')))
            s2+=i
        else:
            s2+=i
        o = open(output, "w")
        o.write(s2)
        o.close()

def affineDecryption(input, output, a, b):
    f = open(input, "r")
    s = f.read()
    s2 = ""
    for i in range(0, 25):
        if (i * int(a)) % 26 == 1:
            a = i
            print(a)
            break
    for i in s:
        if i.isalpha() and i.isupper():
            i = chr((((int(a) * ((((ord(i) - ord('A')) - int(b)) + 26) % 26)) % 26) + ord('A')))
            s2+=i
        elif i.isalpha() and i.islower():
            i = chr((((int(a) * ((((ord(i) - ord('a')) - int(b)) + 26) % 26)) % 26) + ord('a')))
            s2+=i
        else:
            s2+=i
        o = open(output, "w")
        o.write(s2)
        o.close()

def vigenereEncryption(input, output, key):
    f = open(input, "r")
    s = f.read()
    s2 = ""
    s3 = ""
    k = len(key)
    for i in range (0, len(s)):
        s3 += key[i%k]

    for i in range(0, len(s)):
        if s[i].isalpha() and s[i].isupper():
           x  = chr(((ord(s[i]) + ord(s3[i]) - 2 * ord('A')) % 26)+ord('A'))
           s2+=x
        elif s[i].isalpha() and s[i].islower():
            x= chr(((ord(s[i]) + ord(s3[i]) - 2 * ord('a')) % 26) + ord('a'))
            s2+= x
        else:
            s2+=s[i]
        o = open(output, "w")
        o.write(s2)
        o.close()

def vigenereDecryption(input, output, key):
    f = open(input, "r")
    s = f.read()
    s2 = ""
    s3 = ""
    k = len(key)
    for i in range (0, len(s)):
        s3 += key[i%k]

    for i in range(0, len(s)):
        if s[i].isalpha() and s[i].isupper():
           x  = chr(((ord(s[i]) - ord(s3[i]) - 2 * ord('A') + 78) % 26)+ord('A'))
           s2+=x
        elif s[i].isalpha() and s[i].islower():
            x= chr(((ord(s[i]) - ord(s3[i]) - 2 * ord('a') + 78) % 26) + ord('a'))
            s2+= x
        else:
            s2+=s[i]
        o = open(output, "w")
        o.write(s2)
        o.close()

s = sys.argv[1]
s = s.lower()
if s[0] == 'a':
    x = sys.argv[2]
    x.lower()
    if x[0] == 'e':
        affineEncryption(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif x[0] == 'd':
        affineDecryption(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else: print("Check arguments")
elif s[0] == 's':
    x = sys.argv[2]
    x.lower()
    if x[0] == 'e':
        shiftEncryption(sys.argv[3], sys.argv[4], sys.argv[5])
    elif x[0] == 'd':
        shiftDecryption(sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("Check arguments")
elif  s[0] == 'v':
    x = sys.argv[2]
    x.lower()
    if x[0] == 'e':
        vigenereEncryption(sys.argv[3], sys.argv[4], sys.argv[5])
    elif x[0] == 'd':
        vigenereDecryption(sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("Check arguments")


