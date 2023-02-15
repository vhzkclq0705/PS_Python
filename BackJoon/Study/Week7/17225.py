# Silver 1 - 세훈이의 선물가게

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

a, b, n = map(int, input().split())
hq = []
B, R = [], []
end_B, end_R = 1, 1

for _ in range(n):
    time, color, cnt = input().rstrip().split()
    time, cnt = int(time), int(cnt)

    if color == 'B' and end_B > time:
        time = end_B
    elif color == 'R' and end_R > time:
        time = end_R
    
    for i in range(cnt):
        if color == 'B':
            heappush(hq, (time + i * a, color))
        else:
            heappush(hq, (time + i * b, color))

    if color == 'B':
        end_B = time + a * cnt
    else:
        end_R = time + b * cnt

for i in range(len(hq)):
    time, color = heappop(hq)

    if color == 'B':
        B.append(i + 1)
    else:
        R.append(i + 1)

print(len(B))
print(*B)
print(len(R))
print(*R)