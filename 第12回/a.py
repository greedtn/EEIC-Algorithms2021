N, M = map(int, input().split())
edges = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    edges[u-1][v-1] = c

print(edges)


max_flow = 0

def dfs_ff(s, e, flow):
    if (s == e):
        return flow
    visited[s] = True

    for i in range(N):
        if (visited[i] == False) and (edges[s][i] > 0):
            d = dfs_ff(i, e, min(flow, edges[s][i]))
            if d > 0:
                edges[s][i] -= d
                edges[i][s] += d
                return d

while True:
    visited = [False for _ in range(N)]
    f = dfs_ff(0, N-1, 10**9)
    if not f: 
        break
    max_flow += f

print(max_flow)
