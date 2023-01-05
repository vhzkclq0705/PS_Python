# Silver 2 - 스타트와 링크

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
start = []
l = n // 2
diff = 10e9

def bt(depth):
    global diff
    if depth == l:
        sum_Start, sum_Link = 0, 0
        link = [i for i in range(n) if i not in start]

        for i in range(l):
            for j in range(l):
                sum_Start += stats[start[i]][start[j]]
                sum_Link += stats[link[i]][link[j]]

        diff = min(diff, abs(sum_Start - sum_Link))
        return
    
    for i in range(n):
        if i in start or (start and start[-1] > i): continue
        
        start.append(i)
        bt(depth + 1)
        start.pop()

bt(0)
print(diff)