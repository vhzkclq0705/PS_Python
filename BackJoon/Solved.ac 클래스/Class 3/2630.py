# Silver 2 - 색종이 만들기

def divide(n, x, y):
    p = paper[x][y]

    m = n // 2
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != p:
                divide(m, x, y)
                divide(m, x, y + m)
                divide(m, x + m, y)
                divide(m, x + m, y + m)
                return
    
    colour[p] += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
colour = [0, 0]

divide(n, 0, 0)

print(colour[0])
print(colour[1])