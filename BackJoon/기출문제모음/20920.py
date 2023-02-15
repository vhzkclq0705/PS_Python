# Silver 3 - 영단어 암기는 괴로워

from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word = []

for _ in range(n):
    s = input().rstrip()
    if len(s) >= m:
        word.append(s)

word = dict(Counter(word))
word = sorted(word.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for i in word:
    print(i[0])