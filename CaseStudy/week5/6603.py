import sys
input = sys.stdin.readline

def dfs(start, index):
    if start == 6:
        print(*ans)
        return

    for i in range(index, k):
        ans.append(s[i])
        dfs(start + 1, i + 1)
        ans.pop()

while True:
    k, *s = map(int, input().split())
    if k == 0:
        break

    ans = []

    dfs(0, 0)
    print()