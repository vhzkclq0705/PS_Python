def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    ans = [50, 50, 0, 0]
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                ans[0] = min(ans[0], i)
                ans[1] = min(ans[1], j)
                ans[2] = max(ans[2], i + 1)
                ans[3] = max(ans[3], j + 1)
            
    return ans