# Silver 1 - 1, 2, 3 더하기 2

import sys
input = sys.stdin.readline

def bt(tmp):
    tmp = list(tmp)
    if sum(tmp) == n:
        ans.append(tmp)
        return
    elif sum(tmp) > 11:
        return
    
    for i in range(1, 4):
        tmp.append(i)
        bt(tmp)
        tmp.pop()

n, k = map(int, input().split())
ans = []
bt([])
print('+'.join(map(str, sorted(ans)[k - 1])) if k <= len(ans) else -1)