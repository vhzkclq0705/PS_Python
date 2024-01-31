# Silver 1 - 볼 모으기

def move(right, color):
    tmp = ball.rstrip(color) if right else ball.lstrip(color)
    ans.append(tmp.count(color))

n = int(input())
ball = input()
ans = []

move(True, 'R')
move(True, 'B')
move(False, 'R')
move(False, 'B')

print(min(ans))