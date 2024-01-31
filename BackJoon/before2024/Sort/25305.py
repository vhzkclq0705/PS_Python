# Bronze 2 - 커트라인

n, k = map(int, input().split())
scores = sorted(list(map(int, input().split())), reverse=True)

print(scores[k - 1])