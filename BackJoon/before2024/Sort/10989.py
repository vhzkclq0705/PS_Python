# Bronze 1 - 수 정렬하기 3(계수 정렬)

import sys
input = sys.stdin.readline

cnt = [0] * 10001
for _ in range(int(input())):
    cnt[int(input())] += 1

for i in range(10001):
    if cnt[i] > 0:
        for j in range(cnt[i]):
            print(i)