import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
s = int(input())
ans = []
bun = degi = 0
cnt = 2

while True:
    for _ in range(2):
        bun += 1
        ans.append((bun, 0))
        degi += 1
        ans.append((degi, 1))
    for _ in range(cnt):
        bun += 1
        ans.append((bun, 0))
    for _ in range(cnt):
        degi += 1
        ans.append((degi, 1))
    
    if bun > t:
        print(ans.index((t, s)) % n)
        break

    cnt += 1