# Silver 3 - 서강근육맨

import sys
input = sys.stdin.readline

n = int(input())
machines = sorted(list(map(int, input().split())))
ans = 0

if n % 2 == 0:
    for i in range(n // 2):
        ans = max(ans, machines[i] + machines[n - 1 - i])
else:
    ans = max(ans, machines.pop())
    for i in range(n // 2):
        ans = max(ans, machines[i] + machines[n - 2 - i])

print(ans)

# 짧은 버전 - 시간 56 ms
# n = int(input())
# machines = sorted(list(map(int, input().split())))
# ans, m = (0, n) if n % 2 == 0 else (machines[-1], n - 1)

# for i in range(n // 2):
#     ans = max(ans, machines[i] + machines[m - 1 - i])

# print(ans)