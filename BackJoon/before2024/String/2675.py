# Bronze 2 - 문자열 반복

for _ in range(int(input())):
    n, s = map(str, input().split())
    for i in s:
        print(i * int(n), end='')
    print()