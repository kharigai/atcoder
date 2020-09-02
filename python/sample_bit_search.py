n, w = map(int, input().split())
lst = list(map(int, input().split()))

exit = False
for i in range(2**n):
    total = 0
    for j in range(n):
        if (i>>j)&1 == 1:
           total += lst[j] 
    if total == w:
        exit = True
        break
print('yes' if exit else 'no')
