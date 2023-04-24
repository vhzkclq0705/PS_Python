# LEVEL 2

def solution(places):
    ans = []

    for p in places:
        q = []
        flag = True
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    q.append((i, j))

        for i in range(len(q)):
            for j in range(i+1, len(q)):
                dx = abs(q[i][0]-q[j][0])
                dy = abs(q[i][1]-q[j][1])
                if dx+dy > 2:
                    continue
                elif dx+dy < 2:
                    flag = False
                else:
                    if dx == 2 and p[(q[i][0]+q[j][0])//2][q[i][1]] == 'O':
                        flag = False
                    elif dy == 2 and p[q[i][0]][(q[i][1]+q[j][1])//2] == 'O':
                        flag = False
                    elif dx == dy == 1:
                        maxX = max(q[i][0], q[j][0])
                        maxY = max(q[i][1], q[j][1])
                        if p[maxX][maxY] == 'P':
                            if p[maxX][maxY-1] == 'O' or p[maxX-1][maxY] == 'O':
                                flag = False
                        else: 
                            if p[maxX][maxY] == 'O' or p[maxX - 1][maxY - 1] == 'O':
                                flag = False

        ans.append(int(flag))

    return ans