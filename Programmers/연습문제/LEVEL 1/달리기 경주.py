# LEVEL 1

def solution(players, callings):
    rank = {i: p for i, p in enumerate(players)}
    player = {p: i for i, p in enumerate(players)}
    
    for call in callings:
        now = player[call]
        pre = rank[now-1]
        
        rank[now], rank[now-1] = rank[now-1], rank[now]
        player[pre], player[call] = player[call], player[pre]

    return list(rank.values())