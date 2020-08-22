n = int(input())
if n < 3:
    print(0)
    exit()

lst = [int(n) for n in input().split()]
ct = 0
for i in range(0, n-2):
    for j in range(i+1, n-1): 
        for k in range(j+1, n): 
            l = sorted([lst[i], lst[j], lst[k]])
            if len(set(l)) == 3:
                m = l.pop()
                if m < sum(l):
                    ct += 1
print(ct)
