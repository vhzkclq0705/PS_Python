# Silver 2 - 랭킹전 대기열

import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().rstrip().split()
    l = int(l)
    flag = False

    for room in rooms:
        if len(room) == m or l > room[0][0] + 10 or l < room[0][0] - 10:
            continue
        room.append((l, n))
        flag = True
        break
    
    if not flag:
        rooms.append([(l, n)])

for room in rooms:
    print('Started!' if len(room) == m else 'Waiting!')
    for player in sorted(room, key=lambda x: x[1]):
        print(*player)
    