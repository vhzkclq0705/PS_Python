# Silver 3 - 통계학

import sys
input = sys.stdin.readline

n = int(input())
cnt = [0] * 8002
arr = []
f = []

for _ in range(n):
    num = int(input())
    arr.append(num)
    if num == -4000:
        cnt[0] += 1
    elif num < 0:
        cnt[num * -1] += 1
    elif num == 0:
        cnt[4000] += 1
    else:
        cnt[4000 + num] += 1

max_value = max(cnt)

for i in range(8002):
    if cnt[i] == max_value:
        if i == 0:
            f.append(-4000)
        elif i < 4000:
            f.append(i * -1)
        elif i == 4000:
            f.append(0)
        else:
            f.append(i - 4000)

arr.sort()
f.sort()

print(round(sum(arr) / n))
print(arr[n // 2])
print(f[1]) if len(f) > 1 else print(f[0])
print(arr[-1] - arr[0])