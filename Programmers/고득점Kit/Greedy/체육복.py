# Level 1

def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)

    return n - len(lost_set)

n1 = 5
lost1 = [2, 4]
reserve1 = [1, 3, 5]

print(solution(n1, lost1, reserve1))

n2 = 5
lost2 = [2, 4]
reserve2 = [3]

print(solution(n2, lost2, reserve2))

n3 = 3
lost3 = [3]
reserve3 = [1]

print(solution(n3, lost3, reserve3))