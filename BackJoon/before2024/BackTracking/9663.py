# Gold 4 - N-Queen
# PyPy3로 제출 시 통과

n = int(input())
row = [0] * n
ans = 0

def is_Promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    
    return True

def bt(x):
    global ans
    if x == n:
        ans += 1
    else:
        for i in range(n):
            row[x] = i
            if is_Promising(x):
                bt(x + 1)

bt(0)
print(ans)