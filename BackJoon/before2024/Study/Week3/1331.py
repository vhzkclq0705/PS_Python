# Silver 5 - 나이트 투어

import sys
input = sys.stdin.readline

def is_Valid(x1, x2, y1, y2):
    if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or\
        (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
        return True
        
    return False

visited = []
check = []
flag = True

for _ in range(36):
    s = list(input().rstrip())
    x, y = int(s[1]) - 1, ord(s[0]) - 65
    
    if (check and not is_Valid(check[-1][0], x, check[-1][1], y)) or (x, y) in visited:
        flag = False

    visited.append((x, y))
    check.append((x, y))
    
print("Invalid") if not flag or not is_Valid(check[0][0], check[-1][0], check[0][1], check[-1][1]) else print("Valid")