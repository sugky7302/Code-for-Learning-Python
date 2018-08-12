x = "There ard %d types of people." % 10
binary = "binary" 
do_not = "dont't" 
y = "Those who know %s and those who %s." % (binary,do_not)

print(x)
print(y)

print("I said: %r." % x) # %r 顯示的變量"原始"的數據，%s 顯示的是它的值
print("I also said: '%s'." % y)

hilarious = False 
joke_evaluation = "Isn't that joke so funny?! %r" 

print(joke_evaluation % hilarious)

w = "This is the left side of..." 
e = "a string with a right side." 
print(w + e)