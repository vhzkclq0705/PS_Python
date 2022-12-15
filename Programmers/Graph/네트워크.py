# LEVEL 3

def dfs(n, v, computers, visited):
    visited[v] = True

    for com in range(n):
        if com != v and computers[com][v] == 1 and not visited[com]:
            dfs(n, com, computers, visited)

def solution(n, computers):
    ans = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(n, i, computers, visited)
            ans += 1

    return ans

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 1, 1]]
print(solution(n, computers))