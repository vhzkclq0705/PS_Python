# Silver 4 - 문서 검색

import sys
input = sys.stdin.readline

s = input().rstrip()
a = input().rstrip()
left = 0
ans = 0

while left < len(s)-len(a)+1:
    if s[left:left+len(a)] == a:
        ans += 1
        left += len(a)
    else:
        left += 1

print(ans)