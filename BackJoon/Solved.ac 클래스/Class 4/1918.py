# Gold 2 - 후위 표기식

import sys
input = sys.stdin.readline

a = input().rstrip()
s = []
ans = ""

for i in a:
    if i.isalpha():
        ans += i
    else:
        if i == '(':
            s.append(i)
        elif i == '*' or i == '/':
            while s and (s[-1] == '*' or s[-1] == '/'):
                ans += s.pop()
            s.append(i)
        elif i == '+' or i == '-':
            while s and (s[-1] != '('):
                ans += s.pop()
            s.append(i)
        else:
            while s and (s[-1] != '('):
                ans += s.pop()
            s.pop()

while s:
    ans += s.pop()

print(ans)