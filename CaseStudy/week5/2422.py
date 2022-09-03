import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
no = [[False] * n for _ in range(n)]
ans = 0

for _ in range(m):
    a, b = map(int, input().split())

    no[a - 1][b - 1] = True
    no[b - 1][a - 1] = True

for com in combinations(range(n), 3):
    if not no[com[0]][com[1]] and not no[com[0]][com[2]] and not no[com[1]][com[2]]:
        ans += 1

print(ans)