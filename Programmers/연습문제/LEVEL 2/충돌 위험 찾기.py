# Programmers
# Lv.2 - 충돌위험 찾기

from collections import Counter

def move_point(x1, y1, x2, y2):
    if x2 > x1:
        return (x1 + 1, y1)
    if x2 < x1:
        return (x1 - 1, y1)
    if y2 > y1:
        return (x1, y1 + 1)
    if y2 < y1:
        return (x1, y1 - 1)

def move_robot(points, route):
    time = 0
    path = []
    
    for i in range(len(route) - 1):
        x1, y1 = points[route[i] - 1]
        x2, y2 = points[route[i + 1] - 1]
        
        while (x1, y1) != (x2, y2):
            path.append((x1, y1, time))
            x1, y1 = move_point(x1, y1, x2, y2)
            time += 1
    path.append((x1, y1, time))
    
    return path
    
def solution(points, routes):
    paths = []
    ans = 0
    
    for route in routes:
        paths += move_robot(points, route)
    
    for v in Counter(paths).values():
        if v > 1:
            ans += 1
    
    return ans