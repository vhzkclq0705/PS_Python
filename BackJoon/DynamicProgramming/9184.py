# Silver 2 - 신나는 함수 실행

dp = [[[1] * 21 for _ in range(21)] for _ in range(21)]
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j and j < k:
                dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
            else:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0 :
        print('w({}, {}, {}) = 1'.format(a, b, c))
    elif a > 20 or b > 20 or c > 20:
        print('w({}, {}, {}) = {}'.format(a, b, c, dp[-1][-1][-1]))
    else:
        print('w({}, {}, {}) = {}'.format(a, b, c, dp[a][b][c]))
