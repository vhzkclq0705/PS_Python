# Silver 3 - N과 M (1)

from itertools import permutations

n, m = map(int, input().split())
for per in permutations([i for i in range(1, n + 1)], m):
    print(*per)