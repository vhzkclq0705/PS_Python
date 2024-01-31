# Silver 3 - 삼각형 만들기

import sys
input = sys.stdin.readline

s = sorted([int(input()) for _ in range(int(input()))])

while len(s) > 2:
    c = s.pop()
    a, b = s[-1], s[-2]
    
    if a + b > c:
        print(a+b+c)
        break
else:
    print(-1)