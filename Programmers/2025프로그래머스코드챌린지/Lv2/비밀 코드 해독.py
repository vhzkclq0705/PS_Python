from itertools import combinations

def solution(n, q, ans):
    answer = 0
    combs = combinations([i for i in range(1, n + 1)], 5)
    
    for comb in combs:
        s = set(comb)
        for i in range(len(q)):
            if len(s & set(q[i])) != ans[i]:
                break
        else:
            answer += 1
    
    return answer