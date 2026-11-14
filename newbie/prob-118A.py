# problem 118A
a = input()
r = a.lower()
x = ["a","e","i","o","u","y"]
c = list(r)
for i in r:
    if i in x:
        c.remove(i)
print(".",".".join(c),sep = "")