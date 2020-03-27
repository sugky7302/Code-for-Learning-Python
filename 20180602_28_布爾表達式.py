True and True # True
False and True # False
1 == 1 and 2 == 1 # False
"test" == "test" # True
1 == 1 or 2 != 1 # True
True and 1 == 1 # True
False and 0 != 0 # False
True or 1 == 1 # True
"test" == "testing" # False
1 != 0 and 2 == 1 # False
"test" != "testing" # True
"test" == 1 # False
not (True and False) # True
not (1 == 1 and 0 != 1) # False
not (10 == 1 or 1000 == 1000) # False
not( 1 != 10 or 3 == 4) # False
not ("testing" == "testing" and "Zed" == "Cool Guy") # True
1 == 1 and (not ("testing" == 1 or 1 == 0)) # True
"chunky" == "bacon" and (not (3 == 4 or 3 == 3)) # False
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) # False
a = 1 and "" or "a"  # 有問題，會回傳a
b = (1 and [""] or ["a"])[0]  # 利用list將""包住，這樣python就會認為是true
print(a, b)
print(1 and 2 and 3)
