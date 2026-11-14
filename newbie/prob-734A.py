# problem 734A
n = int(input())
t = input()
if t.count("A")==t.count("D"):
    print("Friendship")
elif t.count("A")>t.count("D"):
    print("Anton")
else:
    print("Danik")