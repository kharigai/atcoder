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

## 配列の最大値(カンマ区切りでも OK max(1, 2, 3))
>>> max(lst)
10

## 配列の最小値(カンマ区切りでも OK min(1,2 3))
>>> max(lst)
7

## ゼロ埋め 
## [Pythonで文字列・数値をゼロ埋め（ゼロパディング）](https://note.nkmk.me/python-zero-padding/)
>>> '123'.zfill(5)
'00123'

# lib


## union find
## https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
