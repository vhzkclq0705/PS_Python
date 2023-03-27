# LEVEL 1

def solution(s):
    d = dict()
    answer = []
    
    for i in range(len(s)):
        answer.append(-1 if s[i] not in d else i - d[s[i]])
        d[s[i]] = i
        
    return answer