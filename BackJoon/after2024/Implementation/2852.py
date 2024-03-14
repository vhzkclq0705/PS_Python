# Silver 3 - NBA 농구

import sys
input = sys.stdin.readline

n = int(input())
score = [0] * 2880
cnt = [0] * 2
ans = [0] * 2

for _ in range(n):
    team, time = input().rstrip().split()
    score[int(time[:2]) * 60 + int(time[3:])] = team

for i in range(2880):
    if score[i] == '1':
        cnt[0] += 1
    elif score[i] == '2':
        cnt[1] += 1
    
    if cnt[0] > cnt[1]:
        ans[0] += 1
    elif cnt[1] > cnt[0]:
        ans[1] += 1

for i in ans:
    print(f"{i // 60:02}:{i % 60:02}")