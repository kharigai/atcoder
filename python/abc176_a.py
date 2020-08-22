n, x, t = map(int, input().split())
tm = (n // x) * t 
if (n % x) != 0:
    tm += t
print(tm)
