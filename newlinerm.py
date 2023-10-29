a = open("puncs.txt").read()
b = " "
for char in a:
    if char != "\n":
        b = b + char
print(b)
