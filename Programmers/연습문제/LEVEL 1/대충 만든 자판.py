# LEVEL 1

def solution(keymap, targets):
    answer = []
    
    a = [1, 2, 3]
    for target in targets:
        cnt = 0
        flag = False
        for i in target:
            mins = []
            for key in keymap:
                idx = key.find(i)
                if idx != -1:
                    mins.append(idx + 1)
            if mins:
                cnt += min(mins)
            else:
                flag = True
        answer.append(-1 if flag else cnt)
            
    return answer