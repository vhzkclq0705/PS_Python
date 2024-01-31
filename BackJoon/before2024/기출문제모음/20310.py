# Silver 3 - 타노스

import sys
input = sys.stdin.readline

s = list(input().rstrip())

for _ in range(s.count('0') // 2):
    s.pop(-s[::-1].index('0') - 1)

for _ in range(s.count('1') // 2):
    s.pop(s.index('1'))

print(*s, sep='')