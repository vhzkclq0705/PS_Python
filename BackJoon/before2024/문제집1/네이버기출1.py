from collections import Counter

def grade(n):
    if n >= 90:
        return 'A'
    elif n >= 80:
        return 'B'
    elif n >= 70:
        return 'C'
    elif n >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    scores = list(zip(*scores))
    ans = ''
    
    for i in range(len(scores)):
        c = Counter(scores[i])
        total = sum(scores[i])
        l = len(scores)
        self = scores[i][i]

        if (self == max(c) or self == min(c)) and c[self] == 1:
            total -= self
            l -= 1
        ans += grade(total / l)
    
    return ans

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))