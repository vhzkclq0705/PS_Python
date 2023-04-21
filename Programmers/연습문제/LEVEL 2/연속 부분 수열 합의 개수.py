# LEVEL 2

def solution(elements):
    ans = set()
    l = len(elements)
    
    for i in range(l):
        tmp = elements[i]
        ans.add(tmp)
        for j in range(i + 1, i + l):
            tmp += elements[j % l]
            ans.add(tmp)
                
    return len(ans)