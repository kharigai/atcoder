n = int(input())

tbl = [0]
ans = 0
for i in range(1, n):
    for j in range(1, i+1):
        if (i % j) == 0:
            ans += 1
print(ans)
