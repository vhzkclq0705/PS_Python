# Silver 1 - 회전 초밥

from collections import defaultdict
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
d = defaultdict(int)
left, right = 0, k - 1
ans = 1
d[c] += 1

for i in range(k):
    d[sushi[i]] += 1

while left < n:
    ans = max(ans, len(d))

    d[sushi[left]] -= 1
    if d[sushi[left]] == 0:
        del d[sushi[left]]
    left += 1

    right += 1
    d[sushi[right % n]] += 1

print(ans)