N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 10**9 + 7

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

dp[0][0] = 1

for i in range(N):
    s = [0]
    for j in range(K+1):
        s.append((s[-1] + dp[i][j]) % MOD)
    for j in range(K+1):
        dp[i+1][j] = (s[j+1] - s[max(0, j - A[i])]) % MOD

print(dp[N][K])