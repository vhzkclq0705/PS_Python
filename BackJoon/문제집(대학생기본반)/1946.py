# Silver 1 - 신입 사원

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    rank = sorted([list(map(int, input().split())) for _ in range(n)])
    top = 0
    ans = 1

    for i in range(1, n):
        if rank[i][1] < rank[top][1]:
            top = i
            ans += 1

    print(ans)