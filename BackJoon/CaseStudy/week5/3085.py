import sys
input = sys.stdin.readline

def check():
    maxValue = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if graph[i][j] == graph[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            maxValue = max(maxValue, cnt)

        cnt = 1
        for j in range(1, n):
            if graph[j][i] == graph[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            maxValue = max(maxValue, cnt)
    
    return maxValue

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
            ans = max(ans, check())
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
        
        if i + 1 < n:
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            ans = max(ans, check())
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]

print(ans)