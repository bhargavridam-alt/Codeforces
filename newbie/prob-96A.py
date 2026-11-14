# problem 96A

a = input()
b = "1111111"
c = "0000000"
inc = False
for i in range(len(a)-6):
    if a[i:i+7]==b or a[i:i+7]==c:
        inc = True
        break
print("YES" if inc else "NO")