# input

## 整数
x = int(iput())

## 文字列
x = input()

## スペース区切りの整数を複数の変数に代入
x, y = map(int, input().split())

## スペース木切りの整数を配列に代入
>>> lst = list(map(int, input().split()))
1 2 3
>>> lst
[1, 2, 3]
>>>

>>> lst = [int(n) for n in input().split()]
1 2 3
>>> lst
[1, 2, 3]

## 2次元の配列
k = int(input())
lst = [[int(n) for n in input().split()] for i in range(k)]

>>> k = int(input())
3
>>> lst = [[int(n) for n in input().split()] for i in range(k)]
10 11 12
20 21 22
30 31 32
>>> lst
[[10, 11, 12], [20, 21, 22], [30, 31, 32]]


