# 백준 22864, 피로도, 브론즈 2, 브루트포스
import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
p = 0
ans = 0

if a > d:
    print(0)
else:
    for i in range(24):
        if p > d:
            break
        else:
            if p + a <= d:
                p += a
                ans += b
            else:
                p -= c
                if p < 0:
                    p = 0

    print(ans)