# Silver 3 - N과 M (5)

from itertools import permutations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for p in permutations(nums, m):
    print(*p)