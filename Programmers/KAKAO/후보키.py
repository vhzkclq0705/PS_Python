# LEVEL 2

from itertools import combinations

def solution(relation):
    row, col = len(relation), len(relation[0])

    total = []
    for i in range(1, col + 1):
        total.extend(combinations(range(col), i))

    unique = []
    for t in total:
        tmp = set([tuple(relation[r][c] for c in t) for r in range(row)])
        if len(tmp) == row:
            unique.append(tuple(t))

    ans = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                ans.discard(unique[j])

    return len(ans)