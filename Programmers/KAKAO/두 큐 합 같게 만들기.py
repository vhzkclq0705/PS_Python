# LEVEL 2

from collections import deque

def solution(queue1, queue2):
    ans = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    avg = (sum_q1 + sum_q2) // 2

    while True:
        if ans > len(queue1) * 3:
            return -1
        if sum_q1 == sum_q2 == avg:
            break

        if sum_q1 > sum_q2:
            n = q1.popleft()
            if n > avg:
                return -1
            q2.append(n)
            sum_q1 -= n
            sum_q2 += n
        else:
            n = q2.popleft()
            if n > avg:
                return -1
            q1.append(n)
            sum_q1 += n
            sum_q2 -= n
        ans += 1

    return ans

q1 = [3, 2, 7, 2]
q2 = [4, 6, 5, 1]
print(solution(q1, q2))

q1 = [1, 2, 1, 2]
q2 = [1, 10, 1, 2]
print(solution(q1, q2))

q1 = [1, 1]
q2 = [1, 5]
print(solution(q1, q2))