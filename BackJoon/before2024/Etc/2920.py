# Bronze 2 - 음계

import sys
input = sys.stdin.readline

s = list(map(int, input().split()))
a = list(range(1, 9))
b = list(range(8, 0, -1))

if s == a:
    print('ascending')
elif s == b:
    print('descending')
else:
    print('mixed')