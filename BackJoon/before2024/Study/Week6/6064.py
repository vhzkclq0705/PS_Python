# Silver 1 - 카잉 달력

import sys, math
input = sys.stdin.readline

# x에 m씩 더하다가 y를 빼고 n으로 나눈 나머지가 0인 수 찾기 -> 빠름
for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    while x <= m * n:
        if (x - y) % n == 0:
            print(x)
            break
        x += m
    else:
        print(-1)

# x에 m씩, y에 n씩 더하며 공통 부분 찾기 -> 엄청 오래걸림
# for _ in range(int(input())):
#     m, n, x, y = map(int, input().split())
#     LCM = math.lcm(m, n)
#     s = set()

#     for i in range(x, LCM + 1, m):
#         s.add(i)
    
#     for i in range(y, LCM + 1, n):
#         if i in s:
#             print(i)
#             break
#     else:
#         print(-1)