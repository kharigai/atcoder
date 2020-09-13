n = int(input())

a = 1
ans = 10**9 + 1
while a*a < n:
    if n%a == 0:
        ans = min(max(a, n//a), ans)
    a += 1
print(ans)
