# Programmers
# Lv.2 - 마법의 엘리베이터

def solution(storey):
    storey = list(map(int, str(storey)))
    ans = 0
    
    for i in range(len(storey) - 1, 0, -1):
        if (storey[i] == 5 and storey[i - 1] < 5) or storey[i] < 5:
            ans += storey[i]
        else:
            ans += 10 - storey[i]
            storey[i - 1] += 1
    ans += 10 - storey[0] + 1 if storey[0] > 5 else storey[0]
    
    return ans