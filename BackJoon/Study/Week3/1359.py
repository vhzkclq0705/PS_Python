# Silver 4 - 복권

# 코드는 짧으나 조금 더 느림
from itertools import combinations
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
s = range(1, n + 1)
c = list(combinations(s, m))
cnt = 0

for i in c:
    for j in c:
        if len(set(i) & set(j)) >= k:
            cnt += 1

print(cnt / len(c) ** 2)

# 코드는 기나 조금 더 빠름
from itertools import combinations
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
s = list(range(1, n + 1))
cnt = 0

for i in combinations(s, m):
    for j in combinations(s, m):
        tmp = 0
        for x in i:
            if x in j:
                tmp += 1
            if tmp == k:
                cnt += 1
                break

print(cnt / len(list(combinations(s, m))) ** 2)