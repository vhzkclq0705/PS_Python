# Level 2

def solution(name):
    ans = 0
    horizontal = len(name)
    next = 0
    
    for idx, char in enumerate(name):
        ans += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        next = idx + 1
        
        while next < len(name) and name[next] == 'A':
            next += 1
        
        horizontal = min(horizontal, 2 * idx + len(name) - next, idx + 2 * (len(name) - next))
    
    return ans + horizontal

name = "AAAA"
print(solution(name))

name = "JEROEN"
print(solution(name))

name = "JAN"
print(solution(name))