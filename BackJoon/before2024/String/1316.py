# Silver 5 - 그룹 단어 체커

t = int(input())
cnt = 0

for _ in range(t):
    s = list(input())
    word = []

    for i in s:
        if i not in word:
            word.append(i)
        elif i != word[-1]:
            cnt += 1
            break

print(t - cnt)
