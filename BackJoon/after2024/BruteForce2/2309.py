# Bronze 1 - 일곱 난쟁이

from itertools import combinations

tall = [int(input()) for _ in range(9)]

for com in combinations(tall, 7):
    if sum(com) == 100:
        print('\n'.join(map(str, sorted(com))))
        break