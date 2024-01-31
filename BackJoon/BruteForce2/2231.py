# Bronze 2 - 분해합

n = int(input())
m = n
ans = 0

while m > 0:
    if sum(map(int, str(m))) + m == n:
        ans = m
    m -= 1

print(ans)