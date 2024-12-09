# Programmers
# Lv.2 - 광물 캐기

d = {'diamond': [1, 5, 25], 'iron': [1, 1, 5], 'stone': [1, 1, 1]}
ans = 15 * 25 * 50

def calculate(pick, minerals):
    cnt = 0
    for mineral in minerals:
        cnt += d[mineral][pick]
    return cnt

def dfs(i, dia, iron, stone, minerals, total):
    if i == len(minerals) or (dia + iron + stone) == 0:
        global ans
        ans = min(ans, total)
        return
    
    if dia:
        dfs(i + 1, dia - 1, iron, stone, minerals, total + calculate(0, minerals[i]))
    if iron:
        dfs(i + 1, dia, iron - 1, stone, minerals, total + calculate(1, minerals[i]))
    if stone:
        dfs(i + 1, dia, iron, stone - 1, minerals, total + calculate(2, minerals[i]))
        
def solution(picks, minerals):
    minerals_sep = [minerals[i: i + 5] for i in range(0, len(minerals), 5)]
    dfs(0, picks[0], picks[1], picks[2], minerals_sep, 0)
    
    return ans