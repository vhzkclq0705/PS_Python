# LEVEL 1

def solution(lottos, win_nums):
    cor = len(set(lottos) & set(win_nums))
    rank = 7 - cor if cor > 1 else 6
    return [max(1, rank - lottos.count(0)), rank]