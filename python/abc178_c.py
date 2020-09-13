n = int(input())
if n <= 1:
    print(0)
    exit()
print((2**n // 2 - 2) % (10**9 + 7))
