from sys import argv

script,input_file = argv

def print_all(f):
  print(f.read())

def rewind(f):
  f.seek(0)

def print_a_line(line_count,f):
  f = f.readline()
  print(line_count,f.strip())
  # 如果直接用 print(line_count,f.readline()) 而沒有再用strip把空格去掉，顯示出來每行都會空一行。

current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")
current_line = 1
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line,current_file)