# 백준 11508, 2+1 세일, 실버4
import sys
input = sys.stdin.readline

n = int(input())
costs = list(int(input()) for _ in range(n))
total = 0
cnt = 2

costs.sort(reverse = True)

for i in costs:
    if cnt == 0:
        cnt += 2
        continue
    total += i
    cnt -= 1


print(total)