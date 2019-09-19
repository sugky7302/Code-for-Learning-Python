# 不能輸入 print+空格+"XXX"，會出現問題

print("Hello World!")
print("Hello Again")
print("I like typing this.")
# print("This is fun.")
print("Yay! Printing.")
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

if 0:
    print("y")

a = "-16.72,1.39,0.541289"
b = a.split(',')
print(abs(float(b[0]) / 100 - 0.15))
