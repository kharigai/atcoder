x = int(input())

q1, m1 = divmod(x, 500)
print(q1*1000 + (m1//5)*5)

