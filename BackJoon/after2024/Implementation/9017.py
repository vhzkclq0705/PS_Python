# Silver 3 - 크로스 컨트리

import sys
from collections import Counter, defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    rank = list(map(int, input().split()))
    cnt = Counter(rank)
    team = defaultdict(list)
    total, ans = defaultdict(int), defaultdict(int)
    score = 1

    for i in rank:
        if cnt[i] > 5:
            if len(team[i]) < 5:
                team[i].append(score)
            if len(team[i]) < 5:
                total[i] += score
            score += 1
    
    min_score = min(total.values())
    for k, v in total.items():
        if v == min_score:
            ans[k] = team[k][-1]

    print(sorted(ans.items(), key=lambda x: x[1])[0][0])