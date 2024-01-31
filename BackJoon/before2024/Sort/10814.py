# Silver 5 - 나이순 정렬

s = [list(map(str, input().split())) for _ in range(int(input()))]
for i in sorted(s, key=lambda x: int(x[0])):
    print(*i, sep=' ')