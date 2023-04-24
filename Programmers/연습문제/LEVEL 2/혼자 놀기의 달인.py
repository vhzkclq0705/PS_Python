# LEVEL 2

def solution(cards):
    group = [0]
    visited = [False] * len(cards)
    
    for i in range(len(cards)):
        if visited[i]:
            continue
        now = i
        tmp = 0
        while not visited[now]:
            visited[now] = True
            now = cards[now] - 1
            tmp += 1
        group.append(tmp)
    
    group.sort(reverse=True)
    
    return group[0] * group[1]