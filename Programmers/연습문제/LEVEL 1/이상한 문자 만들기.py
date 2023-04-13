# LEVEL 1

def solution(s):
    ans = ''
    s = s.split(' ')
    
    for i in s:
        for j in range(len(i)):
            ans = ans + i[j].upper() if j % 2 == 0 else ans + i[j].lower()
        ans += ' '
    
    return ans[:-1]
                