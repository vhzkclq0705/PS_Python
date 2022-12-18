# Level 1

def solution(array, commands):
    ans = []
    
    for i, j, k in commands:
        ans.append(sorted(array[i - 1: j])[k - 1])
    
    return ans

a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(a, c))