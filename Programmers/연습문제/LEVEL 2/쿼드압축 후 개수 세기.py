# LEVEL 2

def divide(arr, x, y, n):
    global ans
    num = arr[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                for k in range(2):
                    for l in range(2):
                        divide(arr, x+k*n//2, y+l*n//2, n//2)
                return
    
    ans[num] += 1

def solution(arr):
    global ans
    ans = [0, 0]
    divide(arr, 0, 0, len(arr))
    
    return ans