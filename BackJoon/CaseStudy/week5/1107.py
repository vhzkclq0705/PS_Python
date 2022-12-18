import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = list(map(int, input().split()))
ans = abs(100 - n)

for num in range(1000001):
    num = str(num)

    for j in range(len(num)):
        if int(num[j]) in s:
            break
        if j == len(num) - 1:
            ans = min(ans, abs(int(num) - n) + len(num))

print(ans)