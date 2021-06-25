from collections import deque

N, M = map(int, input().split())
S = input()
INF = 10**18
edges = [[] for _ in range(N)]

s = []

for _ in range(M):
    inp = input().split()
    u = int(inp[0])
    v = int(inp[1])
    t = int(inp[2])
    c = inp[3]
    if c == S[0]:
        s.append(u-1)
        s.append(v-1)
    edges[u-1].append([v-1, t, c])
    edges[v-1].append([u-1, t, c])

ANS = INF

s_unique = list(set(s))

dp = [[INF for _ in range(len(S)+1)] for _ in range(N)]

for i in range(N):
    dp[i][0] = 0

for i in s_unique:

    q = deque()
    q.append([i, 0])
    cnt = 1
    while q and cnt <= 100000 :
        tmp = q.popleft()
        now = tmp[0]
        now_s = tmp[1]
        if now_s >= len(S):
            continue
        for e in edges[now]:
            if e[2] == S[now_s]:
                if dp[e[0]][now_s+1] > dp[now][now_s] + e[1]:
                    dp[e[0]][now_s+1] = dp[now][now_s] + e[1]
                    q.append([e[0], now_s+1])
            else:
                if dp[e[0]][now_s] > dp[now][now_s] + e[1]:
                    dp[e[0]][now_s] = dp[now][now_s] + e[1]
                    q.append([e[0], now_s])
        cnt += 1

for i in range(N):
    ANS = min(ANS, dp[i][len(S)])
if ANS == INF:
    print(-1)
else:
    print(ANS)




