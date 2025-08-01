import sys

input = sys.stdin.readline
n, m = list(map(int, input().strip().split()))

baguni = [i+1 for i in range(n)]
for _ in range(m):
    line = input().strip()
    value = list(map(int, line.split()))
    x, y = value[0], value[1]

    if x == 1:
        baguni = baguni[:x-1] + baguni[y-1::-1] + baguni[y:]
    else:
        baguni = baguni[:x-1] + baguni[y-1:x-2:-1] + baguni[y:]

for element in baguni:
    print(element, end=' ')