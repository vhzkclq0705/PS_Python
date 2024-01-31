# Silver 1 - 가장 가까운 세 사람의 심리적 거리
# 이상한 문제 -> 같은 mbti가 3명, 다른 mbti가 1명이어도 답이 0이 아님.

import sys
from itertools import combinations
input = sys.stdin.readline

def distance(a, b):
    dis = 0
    for i, j in zip(a, b):
        if i != j:
            dis += 1
    return dis

for _ in range(int(input())):
    n = int(input())
    mbti = input().rstrip().split()

    if n > 32:
        print(0)
        continue

    ans = 13
    for a, b, c in combinations(mbti, 3):
        cnt = 0
        cnt += distance(a, b)
        cnt += distance(a, c)
        cnt += distance(b, c)
        
        ans = min(ans, cnt)
    print(ans)