# LEVEL 2

from collections import deque

d = {')':'(', '}':'{', ']':'['}

def check(s):
    q = s.copy()
    c = []

    while q:
        blank = q.pop()
        if blank in d:
            c.append(blank)
        else:
            if not c:
                return 0
            else:
                if blank != d[c.pop()]:
                    return 0

    return 1 if not c else 0

def solution(s):
    s = deque(s)
    ans = []

    for i in range(len(s)):
        s.rotate(-1)
        ans.append(check(s))

    return sum(ans)