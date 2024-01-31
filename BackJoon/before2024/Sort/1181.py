# Silver 5 - 단어 정렬

words = set([input() for _ in range(int(input()))])
print(*sorted(words, key=lambda x: (len(x), x)), sep='\n')