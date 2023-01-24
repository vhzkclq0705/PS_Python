# Silver 2 - 에디터

from collections import deque
import sys
input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()

for _ in range(int(input())):
    a = input().rstrip()
    
    if a == "L" and left:
        right.appendleft(left.pop())
    elif a == "D" and right:
        left.append(right.popleft())
    elif a == "B" and left:
        left.pop()
    elif a[0] == "P":
        left.append(a[2])    

print(''.join(left + right))