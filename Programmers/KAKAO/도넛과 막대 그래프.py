# LEVEL 2

from collections import defaultdict

def solution(edges):
    answer = [0] * 4
    cnt = defaultdict(lambda: [0, 0])
    
    for s, e in edges:
        cnt[s][0] += 1
        cnt[e][1] += 1
    
    for k, v in cnt.items():
        if v[0] >= 2 and v[1] == 0:
            answer[0] = k
        elif v[0] == 0 and v[1] >= 1:
            answer[2] += 1
        elif v[0] == 2 and v[1] >= 2:
            answer[3] += 1
    
    answer[1] = cnt[answer[0]][0] - answer[2] - answer[3]
    
    return answer