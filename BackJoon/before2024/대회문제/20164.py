# Gold 5 - 홀수 홀릭 보석

import sys
input = sys.stdin.readline

def cnt_odd(n):
    return sum([1 for i in n if int(i) % 2 == 1])

def dfs(n, cnt):
    global ans_min, ans_max
    cnt += cnt_odd(n)
    l = len(n)

    if l == 1:
        ans_min = min(ans_min, cnt)
        ans_max = max(ans_max, cnt)
        return
    elif l == 2:
        tmp = int(n[0]) + int(n[1])
        dfs(str(tmp), cnt)
    else:
        for i in range(1, l):
            for j in range(i + 1, l):
                tmp = int(n[:i]) + int(n[i:j]) + int(n[j:])
                dfs(str(tmp), cnt)

n = input().rstrip()
ans_min = sys.maxsize
ans_max = 0

dfs(n, 0)
print(ans_min, ans_max)