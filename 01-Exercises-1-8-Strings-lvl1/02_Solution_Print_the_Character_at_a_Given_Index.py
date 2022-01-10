hello = "Hello"
i = 4

# index start from 0 (not with 1)
# hello   = len = 5(total)
# 01234   = i = 4

if i < len(hello):
    print(hello[i])
    # will print "o"

empty = ""
if len(empty) == 0:
    print("Empty String")
    # this will print Empty String if == 0

# index: 0123456789
value = "World"
i = 9
if i > len(value):
    print("i is out of range")
    # this will print "i is out of range"
