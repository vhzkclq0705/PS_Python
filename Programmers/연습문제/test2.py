def solution(width, height, diagonals):
    dp = [[0] * (width + 1) for _ in range(height + 1)]

    for i in range(height + 1):
        for j in range(width + 1):
            if (i and not j) or (j and not i):
                dp[i][j] = 1
    
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 10000019

    return (dp[-1][-1]) * len(diagonals)

print(solution(2, 2, [[1, 1], [2, 2]]))
print(solution(51, 37, [[17, 19]]))