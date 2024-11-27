# BOJ
# G5 - 2212(센서)

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = sorted(map(int, input().split()))
dist = sorted([sensor[i] - sensor[i - 1] for i in range(1, n)])

print(sum(dist[:n - k]))