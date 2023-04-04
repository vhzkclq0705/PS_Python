# LEVEL 1

def solution(babbling):
    answer = 0
    words = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        for w in words:
            if w * 2 not in i:
                i = i.replace(w, ' ')
        if i.strip() == '':
            answer += 1
        
    return answer