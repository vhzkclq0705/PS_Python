# Silver 4 - 걷기

import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

if 2 * w <= s:
    print((x + y) * w)
else:
    MIN = min(x, y)
    ABS = abs(x - y)
    ans = MIN * s

    if w > s:
        ans = ans + ABS * s if ABS % 2 == 0 else ans + (ABS - 1) * s + w
    else:
        ans += ABS * w
    print(ans)