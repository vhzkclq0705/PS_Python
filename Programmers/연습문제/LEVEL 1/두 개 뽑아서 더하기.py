# LEVEL 1

def solution(numbers):
    from itertools import combinations
    return sorted((set([sum(i) for i in combinations(numbers, 2)])))