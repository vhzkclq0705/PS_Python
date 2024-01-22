# Silver 5 - 사과 담기 게임

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = 1
ans = 0

for _ in range(int(input())):
    apple = int(input())
    tmp = 0

    if apple < s:
        tmp = s - apple
        s -= tmp
    elif apple > s + m - 1:
        tmp = apple - (s + m - 1)
        s += tmp
    
    ans += tmp

print(ans)