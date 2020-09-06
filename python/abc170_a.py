print (sum(range(6)) - sum(list(map(int, input().split()))))
d = {
    1: 'hon',
    2: 'hon',
    3: 'hon',
    4: 'hon',
}
print(d[int(intpu()) % 10])

def print_end(s):
    print(s)
    exit()

x, y = map(int, input().split())
for i in range(x + 1):
    ii = x - i
    if (i*2 + ii*4) == y:
        print_end('Yes')
print('No')
