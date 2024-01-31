# Silver 1 - 민겸 수

s = input()
m = 0
ans = ['', '']

for i in s:
    if i == 'M':
        m += 1
    else:
        if m:
            ans[0] += str(10 ** m * 5)
            ans[1] += str(10 ** m + 5)
        else:
            ans[0] += '5'
            ans[1] += '5'
        m = 0

if m:
    ans[0] += '1' * m
    ans[1] += str(10 ** (m - 1))

print('\n'.join(ans))