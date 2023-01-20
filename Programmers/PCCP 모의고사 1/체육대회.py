# 2번

# BackTracking
# max_value = 0
# visited = [False] * 10
# total = 0

# def bt(ability, n, m, depth):
#     global total, max_value
#     if depth == m:
#         max_value = max(max_value, total)
#         return
    
#     for i in range(n):
#         if visited[i]:
#             continue
        
#         visited[i] = True
#         total += ability[i][depth]
#         bt(ability, n, m, depth + 1)
#         visited[i] = False
#         total -= ability[i][depth]

# def solution(ability):
#     bt(ability, len(ability), len(ability[0]), 0)
    
#     return max_value

# Permutations
from itertools import permutations

def solution(ability):
    n = len(ability)
    m = len(ability[0])
    ans = 0
    
    for per in permutations(range(n), m):
        total = 0
        for i, p in enumerate(per):
            total += ability[p][i]
        
        ans = max(ans, total)
    
    return ans