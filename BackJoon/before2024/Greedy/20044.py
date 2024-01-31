# Silver - 4

import sys
input = sys.stdin.readline

n = int(input())
s = sorted(list(map(int, input().split())))
print(min([s[i] + s[n*2-1-i] for i in range(n)]))