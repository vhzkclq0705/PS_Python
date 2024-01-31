# Bronze 2 - 분해합

n = int(input())
ans = 0

for num in range(1, n + 1):
    if num + sum(map(int, str(num))) == n:
        ans = num
        break

print(ans)