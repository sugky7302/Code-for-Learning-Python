i = 33
s = 'C'
print(chr(i))
print(ord(s))

print(bytes.fromhex("4330"))
print("43,30,30,31\r\n".strip().replace(',', ''))

def foo():
    print(1/0)

foo()
