# LEVEL 2

def solution(n):
    ans = n + 1
    cnt_n = bin(n).count('1')
    while True:
        if bin(ans).count('1') == cnt_n:
            return ans
        ans += 1