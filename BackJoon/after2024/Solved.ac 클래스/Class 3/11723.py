# Silver 5 - 집합

import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    c = list(input().rstrip().split())

    if c[0] == 'add':
        s.add(c[1])
    elif c[0] == 'remove':
        s.discard(c[1])
    elif c[0] == 'check':
        print(1 if c[1] in s else 0)
    elif c[0] == 'toggle':
        if c[1] in s:
            s.remove(c[1])
        else:
            s.add(c[1])
    elif c[0] == 'all':
        s = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
    else:
        s.clear()