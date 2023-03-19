# LEVEL 1

def cal_day(day):
    y, m, d = map(int, day.split('.'))
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    answer = []
    today = cal_day(today)
    t = dict()
    
    for i in terms:
        a, b = i.split()
        t[a] = int(b) * 28
        
    for i in range(len(privacies)):
        a, b = privacies[i].split()
        if cal_day(a) + t[b] - 1 < today:
            answer.append(i + 1)
        
    return answer