# Bronze 2 - 이진수 덧셈

a, b = input().split()
print(*list(bin(int(a, 2) + int(b, 2)))[2:], sep='')