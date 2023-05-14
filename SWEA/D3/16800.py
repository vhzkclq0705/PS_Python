def find_gcd(n):
    s = set()

    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            s.add((i, n // i))
    
    x, y = sorted(list(s), key=lambda x: abs(x[0] - x[1]))[0]

    return x + y - 2

for t in range(int(input())):
    print(f'#{t + 1} {find_gcd(int(input()))}')