# print(list(reversed([1,2,3,4,5])))

# a = [1,2,3,4,5]

# x, y = 2, 4

# print(a[:x-1] + a[y-1:x-2:-1] + a[y:])

import sys

input = sys.stdin.readline
n, m = int(input().split())

baguni = [i+1 for i in range(n)]
for _ in range(m):
    line = input().strip()
    value = list(map(int, line.split()))
    x, y = value[0], value[1]

    new_list = baguni[:x-1] + baguni[y-1:x-2:-1] + baguni[y:]

print(new_list)