# Silver 3 - 블로그

from collections import defaultdict
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
s = list(map(int, input().split())) + [0]
ans = defaultdict(int)

if sum(s) == 0:
    print('SAD')
else:
    left, right = 0, x - 1
    SUM = sum(s[left:right + 1])
    
    while right < n:
        ans[SUM] += 1
        
        right += 1
        SUM = SUM + s[right] - s[left]
        left += 1
    
    MAX = max(ans)
    print(MAX)
    print(ans[MAX])