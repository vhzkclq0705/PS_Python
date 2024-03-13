# Silver 4 - 스위치 켜고 끄기

import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))
student = [list(map(int, input().split())) for _ in range(int(input()))]

for gen, num in student:
    if gen == 1:
        for i in range(num - 1, n, num):
            switch[i] = 1 - switch[i]
    else:
        left, right = num - 2, num
        switch[num - 1] = 1 - switch[num - 1]

        while left >= 0 and right < n and switch[left] == switch[right]:
            switch[left] = 1 - switch[left]
            switch[right] = 1 - switch[right]
            left -= 1
            right += 1

for i in range(n):
    print(switch[i], end=' ')
    if i in [19, 39, 59, 79]:
        print()
