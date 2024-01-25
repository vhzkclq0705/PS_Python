# Silver 3 - 에너지 드링크

import sys
input = sys.stdin.readline

n = int(input())
energy = sorted(list(map(int, input().split())))

for i in range(n - 1):
    energy[-1] += energy[i] / 2

print(energy[-1])