# Silver 4 - 등수 구하기

import sys
input = sys.stdin.readline

n, score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    rank = sorted([score] + list(map(int, input().split())), reverse=True)
    idx = rank.index(score) + 1

    print(-1 if idx > p or (n == p and score == rank[-1]) else idx)