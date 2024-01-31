# Silver 2 - 주식

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    stock = list(map(int, input().split()))
    max_price = 0
    ans = 0

    for i in range(n - 1, -1, -1):
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            ans += max_price - stock[i]
    
    print(ans)