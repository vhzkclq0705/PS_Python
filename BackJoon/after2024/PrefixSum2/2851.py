# BOJ
# B1 - 2851(슈퍼마리오)

def getABS(n):
    return abs(100 - n)

def solution(mushrooms) -> int:
    ans = 0

    for mushroom in mushrooms:
        ans += mushroom

        if ans == 100:
            break
        if ans > 100 and getABS(ans) > getABS(ans - mushroom):
            ans -= mushroom
            break
    
    return ans

mushrooms = [int(input()) for _ in range(10)]
result = solution(mushrooms)

print(result)