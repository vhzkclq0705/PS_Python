# LEVEL 1

def solution(arr, divisor):
    ans = [i for i in arr if i % divisor == 0]
    return sorted(ans) if ans else [-1]