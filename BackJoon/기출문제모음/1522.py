# Silver 1 - 문자열 교환

import sys
input = sys.stdin.readline

s = input().rstrip()
a_cnt = s.count('a')
l = len(s)
left, right = 0, a_cnt
ans = sys.maxsize

while left < l:
    if right < l:
        ans = min(ans, s[left:right].count('b'))
    else:
        ans = min(ans, (s[left:] + s[:right - l]).count('b'))
    left += 1
    right += 1

print(ans)