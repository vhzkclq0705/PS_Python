# Silver 1 - Z

def start(n, x, y):
    global cnt
    m = 2 ** (n - 1)

    if n == 0:
        return
    
    # 1 quadrant
    if r < x + m and c >= y + m:
        cnt += 4 ** (n - 1)
        start(n - 1, x, y + m)
    # 2 quadrant
    elif r < x + m and c < y + m:
        start(n - 1, x, y)
    # 3 quadrant
    elif r >= x + m and c < y + m:
        cnt += 4 ** (n - 1) * 2
        start(n - 1, x + m, y)
    # 4 quadrant
    else:
        cnt += 4 ** (n - 1) * 3
        start(n - 1, x + m, y + m)

n, r, c = map(int, input().split())
cnt = 0

start(n, 0, 0)
print(cnt)