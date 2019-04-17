str = "43,30,30,31\r\n"
print(len(str))
print(len(str.strip()))
str = str.strip()
str_split = str.split(",")
new_str = str_split[0] + str_split[1] + str_split[2] + str_split[3]
print(bytearray.fromhex(new_str).decode())
print(type(bytearray.fromhex(new_str).decode()))
if new_str != "0000" :
    print("1")
else :
    print("0")