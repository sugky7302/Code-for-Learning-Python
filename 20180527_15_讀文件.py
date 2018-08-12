from sys import argv # 從sys的包中引入argv功能模塊

script,filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again) # open讀的檔名用字串構成

print(txt_again.read())