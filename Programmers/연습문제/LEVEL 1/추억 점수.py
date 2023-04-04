# LEVEL 1

def solution(name, yearning, photo):
    d = {name[i]:yearning[i] for i in range(len(name))}
    return [sum(d[i] for i in p if i in d) for p in photo]