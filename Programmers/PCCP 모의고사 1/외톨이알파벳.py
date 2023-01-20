# 1번

def solution(input_string):
    s = []
    ans = set()
    
    for i in input_string:
        if i in s:
            if s[-1] != i:
                ans.add(i)
        s.append(i)
    
    return ''.join(sorted(ans)) if ans else 'N'