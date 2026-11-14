# problem 122A
n = int(input())
inc = False
l = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
for i in l:
    if n%i==0:
        inc = True
        break
print("YES" if inc else "NO")