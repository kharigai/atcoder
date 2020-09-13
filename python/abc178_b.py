a, b, c, d = map(int, input().split())

ans = -(10**19)

for x in [a, b]:
    for y in [c, d]:
        ans = max(ans, x*y)
print(ans)
