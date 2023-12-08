# Gold 5 - AC

from collections import deque
import sys
input = sys.stdin.readline
    
for _ in range(int(input())):
    func = input().rstrip()
    n = int(input())
    q = deque(input().rstrip()[1:-1].split(','))
    cnt = 0

    for i in func:
        if i == 'D':
            if not q or q[0] == '':
                print('error')
                break
            if cnt % 2 == 1:
                q.pop()
            else:
                q.popleft()
        else:
            cnt += 1
    else:
        if cnt % 2 == 1:
            q.reverse()
        
        print('[' + ",".join(q) + ']')