# Silver 2 - 스택 수열

import sys
input = sys.stdin.readline

s = [int(input()) for _ in range(int(input()))]
stack = []
ans = []
cnt = 1

for i in s:
    while cnt <= i:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    
    if stack.pop() != i:
        print('NO')
        break

    ans.append('-')
else:
    print('\n'.join(ans))