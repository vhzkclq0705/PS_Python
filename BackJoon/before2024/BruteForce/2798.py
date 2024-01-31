# Bronze 2 - 블랙잭

from itertools import combinations

n, m = map(int, input().split())
nums = map(int, input().split())
max_value = 0

for com in combinations(nums, 3):
    total = sum(com)
    if total > max_value and total <= m:
        max_value = total

print(max_value)