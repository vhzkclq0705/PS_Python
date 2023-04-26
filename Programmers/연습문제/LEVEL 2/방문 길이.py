# LEVEL 2

def solution(dirs):
    d = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    ans = set()
    x, y = 0, 0
    
    for i in dirs:
        dx, dy = d[i]
        if -5 <= x+dx <= 5 and -5 <= y+dy <= 5:
            nx, ny = x, y
            x += dx
            y += dy
            ans.add((x, y, nx, ny))
            ans.add((nx, ny, x, y))

    return len(ans) // 2