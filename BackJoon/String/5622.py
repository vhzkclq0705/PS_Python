# Bronze 2 - 다이얼

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
words = input()
ans = 0

for word in words:
    for i in range(len(dial)):
        if word in dial[i]:
            ans += i + 3

print(ans)