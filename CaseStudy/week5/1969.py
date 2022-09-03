import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [list(input().rstrip()) for _ in range(n)]
a = ['A', 'C', 'G', 'T']
cnt = [[0] * 4 for _ in range(m)]
ansString = ""
ansCnt = 0

for i in range(n):
    for j in range(m):
        for k in range(4):
            if s[i][j] == a[k]:
                cnt[j][k] += 1

for i in cnt:
    maxValue = max(i)
    for j in range(4):
        if i[j] == maxValue:
            ansString += a[j]
            maxValue = -1
        elif i[j] > 0:
            ansCnt += i[j]

print(ansString)
print(ansCnt)