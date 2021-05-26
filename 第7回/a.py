N = int(input())
h = list(map(int, input().split()))

INF = 1001001001
dp = [INF] * N
dp[0] = 0


for i in range(N-1):
    dp[i+1] = min(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
    if i < N-2:
        dp[i+2] = min(dp[i+2], dp[i] + abs(h[i] - h[i+2]))

print(dp[N-1])
