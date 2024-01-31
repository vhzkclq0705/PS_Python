# Silver 1 - 에너지 모으기

import sys
input = sys.stdin.readline

def bt(total, w):
    l = len(w)
    if l == 2:
        ans.append(total)
        return
    
    for i in range(1, l - 1):
        tmp = w[i - 1] * w[i + 1]
        e = w.pop(i)
        bt(total + tmp, w)
        w.insert(i, e)

n = int(input())
w = list(map(int, input().split()))
ans = []

bt(0, w)
print(max(ans))