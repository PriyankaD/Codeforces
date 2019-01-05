# http://codeforces.com/contest/1099/problem/A

w,h = map(int,input().split())
u1,d1 = map(int,input().split())
u2,d2 = map(int,input().split())

c = w
for i in range(h, -1, -1):
    c += i
    if i == d1:
        c -= u1
    elif i == d2:
        c -= u2
    if c < 0: c = 0
print(c)
