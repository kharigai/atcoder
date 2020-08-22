n = int(input())
l1 = [0] * n
l2 = [int(n) for n in input().split()]
b = 0
for p in range(1, n):
    s = l2[b] - l2[p] + l1[b]
    if s > 0:
        l1[p] = s
    b = p
print(sum(l1))
