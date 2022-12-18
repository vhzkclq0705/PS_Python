# Level 2

def solution(brown, yellow):
    ans = [0, 0]

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            ans[0] = yellow // i
            ans[1] = i
            if ans[0] * 2 + ans[1] * 2 + 4 == brown:
                ans[0] += 2
                ans[1] += 2
                
                return ans

b1 = 10
y1 = 2
b2 = 8
y2 = 1
b3 = 24
y3 = 24
print(solution(b1, y1))
print(solution(b2, y2))
print(solution(b3, y3))