# Silver 4 - 30번

import sys
input = sys.stdin.readline

def find_num(n):
    s = set([1])

    while n != 1:
        s.add(n)
        if n % 2 == 1:
            n -= 1
        n //= 2

    return s

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(max(find_num(a) & find_num(b)) * 10)