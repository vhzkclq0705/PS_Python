# LEVEL 2

def solution(numbers):
    ans = []

    for n in numbers:
        nb = list('0' + bin(n)[2:])
        idx = ''.join(nb).rfind('0')
        nb[idx] = '1'

        if n % 2 == 1:
            nb[idx+1] = '0'

        ans.append(int(''.join(nb), 2))

    return ans