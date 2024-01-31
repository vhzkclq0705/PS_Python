# Bronze 3 - 삼각형과 세 변

import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    t = sorted([a, b, c])
    if t[0] + t[1] <= t[2]:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or a == c or b == c:
        print('Isosceles')
    elif a != b != c:
        print('Scalene')