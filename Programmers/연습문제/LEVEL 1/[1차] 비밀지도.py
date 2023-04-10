# LEVEL 1

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])[2:].replace('1', '#').replace('0', ' ')
        if len(tmp) < n:
            tmp = ' ' * (n - len(tmp)) + tmp
        answer.append(tmp)
    
    return answer