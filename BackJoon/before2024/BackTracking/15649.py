# Silver 3 - N과 M (1)

# Permutation
from itertools import permutations

n, m = map(int, input().split())
for per in permutations([i for i in range(1, n + 1)], m):
    print(*per)

# BackTracking
n, m = map(int, input().split())
s = []

def bt():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            bt()
            s.pop()

bt()