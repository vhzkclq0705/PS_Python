# Silver 5 - 거스름돈

n = int(input())
ans = 0
while n >= 0:
    if n % 5 == 0:
        ans += n // 5
        break
    n -= 2
    ans += 1

print(-1 if n < 0 else ans)