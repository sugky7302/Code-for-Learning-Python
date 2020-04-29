import re
a = "Expecting property name enclosed in double quotes: line 33 column 5 (char 21)"

print(re.search("line \w+", a).group(0))

b = "$12$"
print(re.search("[$][0-9]+", b))
