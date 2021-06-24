INF = 1001001001

N, M = map(int, input().split())

edges = [[INF] * N for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    edges[u][v] = w

dist = edges

def WF(V, e_list):
    """
    V : node数
    e_list : 隣接リスト
    """

    # dist[i][j]: node(i)からnode(j)へ到達するための最短距離
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
WF(N, edges)

Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    if dist[u][v] == INF:
        print("INF")
    else:
        print(dist[u][v])
