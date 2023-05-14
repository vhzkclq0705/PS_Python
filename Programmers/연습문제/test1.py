def solution(boxes, m, k):
    while k:
        k -= 1
        cost = 0
        for i in boxes:
            tmp = i * m // 10000
            if tmp <= 100000:
                cost = max(cost, tmp)
        m += cost
    
    return m

print(solution([1000, 800, 900], 1000000, 3))
print(solution([9000, 10000, 8520, 9500], 110000, 4))