# 証言テーブルを初期化する
# 最大15人なので 15x15 のテーブルを準備する
# 1人が証言できる最大は15
# -1 は証言なし
# x軸: 人、y軸: 証言
testimonys = [[-1]*15]*15

n = int(input())
for i in range(n):
    for _ in range(int(input())):
        man, testimony = map(int, input().split())
        testimonys[i][man-1] = testimony

# N人が正直者または正直者でないというすべての状態を調べる（bit全探索) 
ans = 0
for i in range(2**n):
    # どこがonかを判定するための領域
    # 1011 の時
    # d = [1, 1, 0, 1]
    d = [0]*n
    for j in range(n):
        if (i>>j)&1: 
            d[j] = 1

    ok = True
    for j in range(n):
        if d[j]:    
            for k in range(n):
                if testimonys[j][k] == -1: continue
                if testimonys[j][k] == d[k]: ok = False
    # バイナリーにして 1 をカウントする
    # >>> bin(3)
    # '0b11'
    # >>> bin(3)[2:]
    # '11'
    # >>> bin(3)[2:].count('1')
    # 2
    if ok:
        ans = max(ans, bin(i)[2:].count('1')) 
print(ans)    
