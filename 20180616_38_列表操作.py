ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 trhings in that lise. Let's fix that.")
stuff = ten_things.split(' ') # 把空格移除，並轉成list儲存。
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10 :
  next_one = more_stuff.pop()
  print("Adding: ", next_one)
  stuff.append(next_one)
  print("There are %d items now." % len(stuff))
  print("There we go: ", stuff)
  print("Let's do some things with stuff.")

  print(stuff[1])
  print(stuff[-1])
  print(stuff.pop())
  print(' '.join(stuff)) # join 是使用一個字符串將列表內容接起來的一個方法。此方法在Python裡是 join(' ',stuff)。
  print('#'.join(stuff[3:5])) # stuff[3:5]是從stuff獲取stuff[3]和stuff[4]，stuff[5]沒有包含其中。