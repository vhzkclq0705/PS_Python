# LEVEL 2

def solution(line):
    s = set()
    l = len(line)
    INF = float('inf')
    minX, maxX, minY, maxY = INF, -INF, INF, -INF
    ans = []
    
    for i in range(l):
        a, b, e = line[i]
        for j in range(i + 1, l):
            c, d, f = line[j]
            if a * d - b * c != 0:
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)
                if a * x + b * y + e == 0 and x == int(x) and y == int(y):
                    minX = min(minX, int(x))
                    maxX = max(maxX, int(x))
                    minY = min(minY, int(y))
                    maxY = max(maxY, int(y))
                    s.add((int(y), int(x)))

    for i in range(maxY, minY - 1, -1):
        tmp = ''
        for j in range(minX, maxX + 1):
            if (i, j) in s:
                tmp += '*'
            else:
                tmp += '.'
        ans.append(tmp)
    
    return ans