a = 15
print(int(a) & 0x01)
print(int(a) & 0x02)
print(int(a) & 0x04)
print(int(a) & 0x08)
print(int(a) & 0x10)
print(int(a) & 0x20)
print(int(a) & 0x80)
print(int(a) & pow(2,7))

print([int(a) & v for v in [1, 2, 4, 8]])

# NOTE: 使用16進位檢測數字，發現只有該bit有值時，print才會>0，不然就=0
