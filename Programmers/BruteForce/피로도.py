# Level 2

from itertools import permutations

def solution(k, dungeons):
    ans = 0

    for p in permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0

        for dungeon in p:
            if hp >= dungeon[0]:
                hp -= dungeon[1]
                cnt += 1
        
        if cnt > ans:
            ans = cnt

    return ans

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))