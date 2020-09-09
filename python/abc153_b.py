h, n = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        if a[i]+a[j] > h:
            print('Yes')
            exit()
print('No')
