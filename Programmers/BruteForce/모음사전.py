# Level 2

from itertools import product

def solution(word):
    ans = []
    s = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6):
        for p in product(s, repeat=i):
            ans.append(''.join(list(p)))
    
    ans.sort()

    return ans.index(word) + 1

word1 = "AAAAE"
print(solution(word1))

word2 = "AAAE"
print(solution(word2))

word3 = "I"
print(solution(word3))

word4 = "EIO"
print(solution(word4))