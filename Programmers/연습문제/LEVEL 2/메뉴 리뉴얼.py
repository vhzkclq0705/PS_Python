# LEVEL 2

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    d = defaultdict(int)
    ans = []

    for o in orders:
        for c in course:
            for com in combinations(list(o), c):
                d[''.join(sorted(com))] += 1

    for c in course:
        tmp = dict(filter(lambda x:len(x[0]) == c and x[1] > 1, d.items()))
        if tmp:
            MAX = max(tmp.values())
            tmp = dict(filter(lambda x:x[1] == MAX, tmp.items()))
            for k in tmp.keys():
                ans.append(k)

    return sorted(ans)