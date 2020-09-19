# n = int(input())
# mod = 10**9+7
# print((10**n - (9**n)*2 + 8**n) % mod)
n = int(input())
mod = 10**9+7
print((pow(10, n, mod) - 2*pow(9, n, mod) + pow(8, n, mod))%mod)
