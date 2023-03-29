# LEVEL 1

def solution(food):
    ans = '0'
    
    for i in range(len(food) - 1, 0, -1):
        cnt = food[i] // 2
        ans = cnt * str(i) + ans + cnt * str(i)
            
    return ans