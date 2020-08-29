k = int(input())
n = 0
for i in range(k):
    n = (n * 10) + 7 
    n = n % k
    if n == 0:
        print(i + 1)
        exit()
print(-1)
