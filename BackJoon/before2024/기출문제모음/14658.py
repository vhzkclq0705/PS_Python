# Gold 3 - 하늘에서 별똥별이 빗발친다

import sys
input = sys.stdin.readline

def check(star):
    global ans
    ls = len(star)

    for i in range(ls):
        cnt = 0
        for j in range(i, ls):
            if star[j] <= star[i] + l:
                cnt += 1
        ans = max(ans, cnt)

    return

n, m, l, k = map(int, input().split())
s = sorted([list(map(int, input().split())) for _ in range(k)])
ans = 0

for i in range(k):
    star = []
    for j in range(i, k):
        if s[j][0] <= s[i][0] + l:
            star.append(s[j][1])
    check(sorted(star))

print(k - ans)