# LEVEL 1

def solution(numbers, hand):
    answer = ''
    now_left, now_right = 10, 11
    d = {0: (3, 1), 10: (3, 0), 11: (3, 2)}
    
    for i in range(3):
        for j in range(3):
            d[i * 3 + j + 1] = (i, j)
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            now_left = i
        elif i in [3, 6, 9]:
            answer += 'R'
            now_right = i
        else:
            dis_left = abs(d[now_left][1] - d[i][1]) + abs(d[now_left][0] - d[i][0])
            dis_right = abs(d[now_right][1] - d[i][1]) + abs(d[now_right][0] - d[i][0])
            if dis_left > dis_right:
                answer += 'R'
                now_right = i
            elif dis_left < dis_right:
                answer += 'L'
                now_left = i
            else:
                if hand == 'left':
                    answer += 'L'
                    now_left = i
                else:
                    answer += 'R'
                    now_right = i
            
    return answer