cnt = 0
for i in range(1, int(input())+1):
    if len(str(i)) % 2:
        cnt += 1
print(cnt)
