# Bronze 1 - 이항 계수 1

from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
print(len(list(combinations(list(range(1, n + 1)), k))))