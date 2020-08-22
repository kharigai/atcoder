# env
$ source ~/.venv/3.8/bin/activate

# input

## 整数
x = int(iput())

## 文字列
x = input()

## 文字列を1文字に分割して配列に代入
>>> lst = list(input())
ABCDE
>>> lst
['A', 'B', 'C', 'D', 'E']

## スペース区切りの整数を複数の変数に代入
x, y = map(int, input().split())

## スペース区切りの整数を配列に代入
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

## 配列の初期化
>>> lst = [0] * 10
>>> lst
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## 配列ソート
>>> lst = [7, 9, 10, 8]
>>> lst.sort()
>>> lst
[7, 8, 9, 10]
>>> lst.sort(reverse=True)
>>> lst
[10, 9, 8, 7]

## ソートした配列を作成する
>>> lst = sorted([7, 9, 10, 8])
>>> lst
[7, 8, 9, 10]

## 配列の sum
>>> sum(lst)
34

## 配列の最大値
>>> max(lst)
10

## 配列の最小値
>>> max(lst)
7
