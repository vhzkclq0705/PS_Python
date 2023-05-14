for t in range(int(input())):
    n = int(input())
    ans = 0
    
    for i in range(n + 1):
        ans += int((n ** 2 - i ** 2) ** .5)
    
    print(f'#{t + 1} {ans * 4 + 1}')