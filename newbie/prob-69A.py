# problem 69A

t = int(input())
a = 0
b = 0
c = 0
for i in range(t):
    a1,b1,c1 = map(int,input().split())
    a += a1
    b += b1
    c += c1
print("YES" if a==0 and b==0 and c==0 else "NO")
