# LEVEL 1

def solution(friends, gifts):
    n = len(friends)
    d = {friends[i]: i for i in range(n)}
    gift_table = [[0] * n for _ in range(n)]
    idx_table = [0] * n
    ans = [0] * n

    for gift in gifts:
        a, b = gift.split()
        gift_table[d[a]][d[b]] += 1
        idx_table[d[a]] += 1
        idx_table[d[b]] -= 1

    for i in range(n):
        for j in range(i + 1, n):
            if gift_table[i][j] > gift_table[j][i]:
                ans[i] += 1
            elif gift_table[i][j] < gift_table[j][i]:
                ans[j] += 1
            else:
                if idx_table[i] > idx_table[j]:
                    ans[i] += 1
                elif idx_table[i] < idx_table[j]:
                    ans[j] += 1

    return max(ans)