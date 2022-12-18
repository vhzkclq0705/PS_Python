# Level 1

import enum


def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3
    ans = []

    for idx, answer in enumerate(answers):
        if answer == a[idx % len(a)]:
            score[0] += 1
        if answer == b[idx % len(b)]:
            score[1] += 1
        if answer == c[idx % len(c)]:
            score[2] += 1
    
    maxScore = max(score)

    for i in range(3):
        if score[i] == maxScore:
            ans.append(i + 1)

    return ans

answers = [1, 3, 2, 4, 2]
print(solution(answers))