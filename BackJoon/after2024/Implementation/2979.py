# Bronze 2 - 트럭 주차

a, b, c = map(int, input().split())
cnt = [0] * 101
ans = 0

for _ in range(3):
    s, e = map(int, input().split())

    for i in range(s, e):
        cnt[i] += 1

for i in range(100):
    if cnt[i] == 1:
        ans += a
    elif cnt[i] == 2:
        ans += b * 2
    elif cnt[i] == 3:
        ans += c * 3

print(ans)