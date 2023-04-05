# LEVEL 1

from collections import Counter

def solution(X, Y):
    answer = ''
    x = dict(Counter(X))
    y = dict(Counter(Y))
    
    for i in range(9, -1, -1):
        i = str(i)
        if i in x and i in y:
            answer += i * min(x[i], y[i])
    
    if not answer:
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer
    