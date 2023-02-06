# Silver 1 - 귀여운 라이언

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
lion = []
left, right = 0, k - 1
ans = sys.maxsize

for i in range(n):
    if s[i] == 1:
        lion.append(i)

if len(lion) < k:
    print(-1)
    exit()

while right < len(lion):
    ans = min(ans, lion[right] - lion[left] + 1)
    left += 1
    right += 1

print(ans)