# Silver 3 - 카드게임

from collections import Counter
import sys
input = sys.stdin.readline

def continuous():
    for i in range(4):
        if num[i] + 1 != num[i + 1]:
            return False
    return True

card = [list(input().split()) for _ in range(5)]
color, num = [], []

for c, n in card:
    color.append(c)
    num.append(int(n))

cnt_color = dict(Counter(color))
cnt_num = dict(Counter(num))
num.sort()
lc, ln = len(cnt_color), len(cnt_num)
sorted_num = sorted(cnt_num.items(), key=lambda x: x[1])

if lc == 1:
    print(num[-1] + 900 if continuous() else num[-1] + 600)
elif ln == 2:
    if sorted_num[0][1] == 1:
        print(sorted_num[1][0] + 800)
    elif sorted_num[0][1] == 2:
        print(sorted_num[1][0] * 10 + sorted_num[0][0] + 700)
elif continuous():
    print(num[-1] + 500)
elif ln == 3:
    if sorted_num[2][1] == 3:
        print(sorted_num[2][0] + 400)
    else:
        if sorted_num[1][0] > sorted_num[2][0]:
            print(sorted_num[1][0] * 10 + sorted_num[2][0] + 300)
        else:
            print(sorted_num[2][0] * 10 + sorted_num[1][0] + 300)
elif ln == 4:
    print(sorted_num[3][0] + 200)
else:
    print(num[-1] + 100)