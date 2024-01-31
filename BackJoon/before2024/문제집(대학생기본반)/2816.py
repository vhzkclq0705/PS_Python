# Bronze 1 - 디지털 티비

import sys
input = sys.stdin.readline

n = int(input())
c = [input().rstrip() for _ in range(n)]
idx1, idx2 = c.index('KBS1'), c.index('KBS2')

if idx1 > idx2: idx2 += 1
print('1' * idx1 + '4' * idx1 + '1' * idx2 + '4' * (idx2 - 1))