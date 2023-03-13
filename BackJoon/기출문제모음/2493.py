# Gold 5 - 탑

import sys
input = sys.stdin.readline

n = int(input())
s = map(int, input().split())
stack = []
ans = []

for idx, v in enumerate(s):
    if not stack:
        ans.append(0)
        stack.append((v, idx))
    else:
        while stack:
            if stack[-1][0] < v:
                stack.pop()
                if not stack:
                    ans.append(0)
                    stack.append((v, idx))
                    break
            else:
                ans.append(stack[-1][1] + 1)
                stack.append((v, idx))
                break

print(*ans)