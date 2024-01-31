# Silver 3 - 주유소

import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
min_price = price[0]
ans = 0

for i in range(n - 1):
    min_price = min(min_price, price[i])
    ans += min_price * dis[i]

print(ans)