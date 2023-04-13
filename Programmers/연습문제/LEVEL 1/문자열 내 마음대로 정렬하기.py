# LEVEL 1

def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n], x))