# LEVEL 1

def solution(number):
    from itertools import combinations
    return sum([1 for i in combinations(number, 3) if sum(i) == 0])