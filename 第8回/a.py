N, W = map(int, input().split())
wv = [map(int, input().split()) for _ in range(N)]
w, v = [list(i) for i in zip(*wv)]

INF = 100100100100

MAX_V = 200 * N

dp = [[INF for _ in range(MAX_V+1)] for _ in range(N+1)]

# dp[i+1][j]: i番目までの品物の中から価値の総和がjになるように選んだ時の重さの総和の最小値

dp[0][0] = 0

for i in range(N):
    for j in range(MAX_V+1):
        if j >= v[i]:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]] + w[i])
        else:
            dp[i+1][j] = dp[i][j]

res = 0
for i in range(MAX_V+1):
    if dp[N][i] <= W:
        res = i
print(res)