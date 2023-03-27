# LEVEL 1

def solution(k, score):
    s = []
    answer = []
    
    for i in score:
        if len(s) < k:
            s.append(i)
        else:
            if i >= s[0]:
                s.pop(0)
                s.append(i)
        s.sort()

        answer.append(s[0])
    
    return answer