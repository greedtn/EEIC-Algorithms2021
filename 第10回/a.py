import heapq
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
heap_q = []
for i in s_unique:
    heapq.heappush(heap_q, [dp[i][0], i, 0])
while heap_q:
    tmp = heapq.heappop(heap_q)
    now = tmp[1]
    now_s = tmp[2]
    if now_s >= len(S):
        continue
    for e in edges[now]:
        if e[2] == S[now_s]:
            if dp[e[0]][now_s+1] > dp[now][now_s] + e[1]:
                dp[e[0]][now_s+1] = dp[now][now_s] + e[1]
                heapq.heappush(heap_q,[dp[e[0]][now_s+1], e[0], now_s+1])
        else:
            if dp[e[0]][now_s] > dp[now][now_s] + e[1]:
                dp[e[0]][now_s] = dp[now][now_s] + e[1]
                heapq.heappush(heap_q,[dp[e[0]][now_s], e[0], now_s])
for i in range(N):
    ANS = min(ANS, dp[i][len(S)])
if ANS == INF:
    print(-1)
else:
    print(ANS)