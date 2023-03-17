# Gold 5 - 용액

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
left, right = 0, n - 1
check = sys.maxsize
ans = [a[left], a[right]]

while left < right:
    diff = a[left] + a[right]
    if abs(diff) < check:
        ans[0] = a[left]
        ans[1] = a[right]
        check = abs(diff)

        if check == 0:
            break

    if diff < 0:
        left += 1
    else:
        right -= 1

print(*ans)