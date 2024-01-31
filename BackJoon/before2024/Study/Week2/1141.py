# Silver 2 - 접두사

import sys
input = sys.stdin.readline

n = int(input())
words = sorted([input().rstrip() for _ in range(n)], key=len)
cnt = 0

for i in range(n):
    flag = False
    for j in range(i + 1, n):
        if words[j][:len(words[i])] == words[i]:
            flag = True
            break
    
    if not flag:
        cnt += 1

print(cnt)