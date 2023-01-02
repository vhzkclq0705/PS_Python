# Silver 5 - 좌표 정렬하기 2

n = sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda x: (x[1], x[0]))
for i in n:
    print(*i, sep=' ')