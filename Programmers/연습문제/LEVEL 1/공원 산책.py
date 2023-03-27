# LEVEL 1

def solution(park, routes):
    n = len(park)
    m = len(park[0])
    x, y = 0, 0
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x = i
                y = j

    for r in routes:
        dir, dis = r.split()
        dis = int(dis)
        if dir == 'E' and 0 <= y + dis < m:
            for i in range(y, y + dis + 1):
                if park[x][i] == 'X':
                    break
            else:
                y += dis
        elif dir == 'W' and 0 <= y - dis < m:
            for i in range(y, y - dis - 1, -1):
                if park[x][i] == 'X':
                    break
            else:
                y -= dis
        elif dir == 'N' and 0 <= x - dis < n:
            for i in range(x, x - dis - 1, -1):
                if park[i][y] == 'X':
                    break
            else:
                x -= dis
        elif dir == 'S' and 0 <= x + dis < n:
            for i in range(x, x + dis + 1):
                if park[i][y] == 'X':
                    break
            else:
                x += dis

    return [x, y]