# Gold 5 - A와 B 2

import sys
input = sys.stdin.readline

def bt(t):
    global ans
    if len(t) == len(s):
        if t == s:
            ans = True
        return
    
    if t[0] == 'B':
        bt(t[:0:-1])
    if t[-1] == 'A':
        bt(t[:-1])

s = input().rstrip()
t = input().rstrip()
ans = False

bt(t)
print(1 if ans else 0)