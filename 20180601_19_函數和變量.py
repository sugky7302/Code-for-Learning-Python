def cheese_and_crackers(cheese_count,boxes_of_crackers):
  print("You have %d cheeses!" % cheese_count)
  print("You have %d boxes of crackers!" % boxes_of_crackers)
  print("Man that's enough for a party!")
  print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 附加題：用10種方法運行一個自定義函數
def additional_exercises(a, b, c):
  print("測試函數： %s, %s, %s" % (a, b, c)) # %d 只能加入number，字符串會出錯

additional_exercises(1,2,3) # 1
additional_exercises(1+2,2-3,4-51) # 2
p, q, r = 10, 20, 30 # 多變數賦值同Lua
additional_exercises(p,q,r) # 3
additional_exercises(p*10, q*5, r+1) # 4
additional_exercises(p*q,q*r, r*p) # 5
additional_exercises(input("a >> "), input("b >> "), input("c >> ")) # 6
n1, n2, n3 = input("n1 >> "), input("n2 >> "), input("n3 >> ")
additional_exercises(n1, n2, n3) # 7
k1 = int(input("k_a >> ")) * int(input("k_b >> ")) # input 出來的是string，所以只要用 int() 把 str 轉成 num 就可以算了
additional_exercises(k1, n2, n3) # 8
from sys import argv # 這要另外開檔

script, filename, first, second, third = argv
additional_exercises(first, second, third) # 9
txt = open(filename)
t1, t2, t3 = txt.readlines()
t1, t2, t3 = t1.strip(), t2.strip(), t3.strip()
additional_exercises(t1, t2, t3) # 10

