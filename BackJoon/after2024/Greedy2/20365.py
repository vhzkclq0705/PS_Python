# Silver 3 - 블로그2

import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
r = ' '.join(s.split('B')).split()
b = ' '.join(s.split('R')).split()

if not r or not b:
    print(1)
else:
    print(min(len(r), len(b)) + 1)