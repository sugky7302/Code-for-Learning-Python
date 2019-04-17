import time 

localtime = time.asctime(time.localtime(time.time()))
s = "Today is %s." % localtime
s += " Hi! What's your name ? My name is %s." % "John"
print(s)