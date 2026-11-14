# problem 520A

n = int(input())
a = input()
b = list(set(list(a.lower())))
if len(b)==26:
    print("YES")
else:
    print("NO")