# LEVEL 2

def solution(n, t, m, p):
    ans = ''
    d = {i:str(i) if i < 10 else chr(i + 55) for i in range(16)}
    
    for i in range(t * m):
        tmp = ''
        a, b = divmod(i, n)

        while a > 0:
            tmp = d[b] + tmp
            a, b = divmod(a, n)
        
        tmp = d[b] + tmp
        ans += tmp
    
    return ''.join([ans[i] for i in range(p - 1, t * m, m)])