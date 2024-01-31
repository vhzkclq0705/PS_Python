# Silver 1 - 곱셈

import sys
input = sys.stdin.readline

def multiply(n, k):
    if k == 1:
        return n % c
    m = multiply(n, k // 2)

    return (m * m * n) % c if k % 2 else (m * m) % c

a, b, c = map(int, input().split())
print(multiply(a, b))