a = open("puncs.txt").read()
punc = "[]{ }:<>?/.,;''|\!@#$"
rm = " "
for char in a:
    if char not in punc:
        rm = rm + char
print(rm)


