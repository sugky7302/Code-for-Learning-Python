haha = "43,30,30,31\r\n"
print(len(haha))
print(len(haha.strip()))
haha = haha.strip()
str_split = haha.split(",")
new_str = str_split[0] + str_split[1] + str_split[2] + str_split[3]
print(bytearray.fromhex(new_str).decode())
print(type(bytearray.fromhex(new_str).decode()))
if new_str != "0000" :
    print("1")
else :
    print("0")

a = "1 2 3 4 5"
print(len(a))
print(a.split(" "))
print(len(a.split(" ")))
print([(k > 0) and int(v) or v for k, v in enumerate(a.split(" "))])

args = [1]
q = [str(arg) for arg in args]
print(len(" ".join(q)))
