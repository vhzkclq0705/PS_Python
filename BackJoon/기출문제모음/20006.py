# Silver 2 - 랭킹전 대기열

import sys
input = sys.stdin.readline

p, m = map(int, input().split())
room = []

for _ in range(p):
    level, id = input().rstrip().split()
    level = int(level)

    if not room:
        room.append([level, m - 1, [(level, id)]])
    else:
        for i in range(len(room)):
            l, c = room[i][0], room[i][1]
            if l - 10 <= level <= l + 10 and c > 0:
                room[i][1] -= 1
                room[i][2].append((level, id))
                break
        else:
            room.append([level, m - 1, [(level, id)]])

for r in room:
    print('Started!' if r[1] == 0 else 'Waiting!')
    for level, id in sorted(r[2], key=lambda x:x[1]):
        print(level, id)