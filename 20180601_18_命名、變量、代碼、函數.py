# this one is like your scripts with argv
def print_two(*args):
  arg1,arg2 = args
  print("arg1: %r, arg2: %r" %(arg1,arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
  print("arg1: %r, arg2: %r" % (arg1,arg2))

# this just takes one argument
def print_one(arg1):
  print("arg1: %r" % arg1)

# this one takes no arguments
def print_none():
  print("I got nothing'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
# print_one("First!","Second!") 只設定一個變量，就不能接受多個變量，不向lua一樣會自動忽略
print_none()