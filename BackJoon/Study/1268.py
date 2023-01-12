# Bronze 1 - 임시 반장 정하기

import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
cnt = [0] * n

for i in range(n):
    for j in range(n):
        for k in range(5):
            if i != j and s[i][k] == s[j][k]:
                cnt[i] += 1
                break

print(cnt.index(max(cnt)) + 1)