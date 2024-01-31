# Silver 3 - N과 M (4)

n, m = map(int, input().split())
s = []

def bt(v):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(v, n + 1):
        s.append(i)
        bt(i)
        s.pop()

bt(1)