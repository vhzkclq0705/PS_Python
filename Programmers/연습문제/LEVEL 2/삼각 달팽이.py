# LEVEL 2

def fill(arr, x, y, idx, n):
    arr[x][y] = idx
    idx += 1
    
    for i in range(x, x+n):
        arr[i][y] = idx
        idx += 1
    for i in range(y+1, y+n):
        arr[x+n-1][i] = idx
        idx += 1
    for i in range(x+n-2, x, -1):
        arr[i][i-y] = idx
        idx += 1
    
    if x+2 < len(arr) and arr[x+2][y+1] == 0:
        fill(arr, x+2, y+1, idx-1, n-3)
    return

def solution(n):
    arr = [[0] * i for i in range(1, n+1)]
    fill(arr, 0, 0, 0, n)
    
    ans = []
    for i in arr:
        ans += i
    
    return ans