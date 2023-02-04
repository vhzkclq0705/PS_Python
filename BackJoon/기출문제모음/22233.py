# Silver 2 - 가희와 키워드

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = {input().rstrip() for _ in range(n)}

for _ in range(m):
    s.difference_update(input().rstrip().split(','))
    print(len(s))