# LEVEL 2

def solution(n, words):
    s = set([words[0]])
    last = words[0]
    
    for i, w in enumerate(words):
        if i == 0:
            continue
        if w in s or w[0] != last[-1]:
            return [i%n+1, i//n+1]
        last = w
        s.add(w)

    return [0, 0]