# Silver 2 - A -> B

a, b = map(int, input().split())
ans = 1

while a < b:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        break

    ans += 1

print(ans if a == b else - 1)