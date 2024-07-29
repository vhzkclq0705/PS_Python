# Gold 5 - 톱니바퀴

from collections import deque

def isLeftTurnable(n, l):
    if n < 0:
        return False
    if wheels[n][2] != l:
        return True
    return False

def isRightTurnable(n, r):
    if n > 3:
        return False
    if wheels[n][6] != r:
        return True
    return False
            
def rotateWheel(n, d):
    if n < 0 or n > 3:
        return
    visited[n] = True
    l, r = wheels[n][6], wheels[n][2]
    wheels[n].rotate(d)

    if isLeftTurnable(n - 1, l) and not visited[n - 1]:
        rotateWheel(n - 1, -d)
    if isRightTurnable(n + 1, r) and not visited[n + 1]:
        rotateWheel(n + 1, -d)
    
wheels = [deque(map(lambda x: int(x), input())) for _ in range(4)]
rotations = [list(map(int, input().split())) for _ in range(int(input()))]

for n, d in rotations:
    visited = [False] * 4
    rotateWheel(n - 1, d)

print(wheels[0][0] * 1 + wheels[1][0] * 2 + wheels[2][0] * 4 + wheels[3][0] * 8)