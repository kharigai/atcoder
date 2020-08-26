n, d = map(int, input().split())

d **= 2
ct = 0
for i in range(n):
    x, y = map(int, input().split())
    if x**2 + y**2 <= d:
        ct += 1
print(ct)
