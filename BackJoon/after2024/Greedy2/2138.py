# Gold 5 - 전구와 스위치

def turn():
    tmp = a[:]
    cnt = 0

    for i in range(1, n):
        if tmp[i - 1] != b[i - 1]:
            cnt += 1
            for j in range(i - 1, i + 2):
                if j < n:
                    tmp[j] = 1 - tmp[j]
    
    return cnt if tmp == b else 100001

n = int(input())
a = list(map(int, input()))
b = list(map(int, input()))

ans = turn()
a[0] = 1 - a[0]
a[1] = 1 - a[1]
ans = min(ans, turn() + 1)

print(-1 if ans == 100001 else ans)