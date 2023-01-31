# Silver 2 - 연산자 끼워넣기 (2)

import sys
input = sys.stdin.readline

def bt(total, op, depth):
    global max_Value, min_Value
    if depth == len(s):
        max_Value = max(max_Value, total)
        min_Value = min(min_Value, total)
        return
    
    if op[0] > 0:
        op[0] -= 1
        bt(total + s[depth], op, depth + 1)
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        bt(total - s[depth], op, depth + 1)
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        bt(total * s[depth], op, depth + 1)
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        bt(total // s[depth] if total > 0 else (total * (-1) // s[depth]) * (-1), op, depth + 1)
        op[3] += 1

n = int(input())
s = list(map(int, input().split()))
op = list(map(int, input().split()))
max_Value = sys.maxsize * (-1)
min_Value = sys.maxsize

bt(s[0], op, 1)
print(max_Value)
print(min_Value)