# Silver 4 - 균형잡힌 세상

import sys
input = sys.stdin.readline

while True:
    s = []
    a = input().rstrip()[:-1]
    if not a:
        break
    
    for i in a:
        if i.isalpha():
            continue

        if i == '(':
            s.append(i)
        elif i == '[':
            s.append(i)
        elif i == ')':
            if not s or s[-1] != '(':
                print('no')
                break
            else:
                s.pop()
        elif i == ']':
            if not s or s[-1] != '[':
                print('no')
                break
            else:
                s.pop()
    else:
        print('no' if s else 'yes')