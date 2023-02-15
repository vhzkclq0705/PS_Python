# Silver 3 - 수 이어 쓰기

from collections import deque
import sys
input = sys.stdin.readline

s = deque(input().rstrip())
i = 0

while True:
    i += 1
    num = deque(str(i))

    while num and s:
        if s[0] == num[0]:
            s.popleft()
        num.popleft()
    
    if not s:
        print(i)
        break