n = int(input())
cnt = 0
for k in [[int(n) for n in input().split()] for i in range(n)]:
    if k[0] == k[1]:
        cnt += 1
        if cnt >= 3:
            print('Yes')
            exit()
    else:
        cnt = 0
print('No')
