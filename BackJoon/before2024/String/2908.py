# Bronze 2 - 상수

a, b = map(str, input().split())
print(max(int(a[::-1]), int(b[::-1])))