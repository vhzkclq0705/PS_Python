# BOJ
# G3 - 20366(같이 눈사람 만들래?)

import sys
input = sys.stdin.readline

n = int(input())
snow = sorted(list(map(int, input().split())))
ans = sys.maxsize

for i in range(n):
    for j in range(i + 3, n):
        snowman_1 = snow[i] + snow[j]
        l, r = i + 1, j - 1
        
        while l < r:
            snowman_2 = snow[l] + snow[r]
            ans = min(ans, abs(snowman_1 - snowman_2))

            if snowman_1 == snowman_2:
                print(0)
                exit()
            if snowman_2 < snowman_1:
                l += 1
            else:
                r -= 1

print(ans)