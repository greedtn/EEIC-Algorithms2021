N, M = map(int, input().split())
S = input()

edges = [[] for _ in range(N)]

for _ in range(M):
    u, v, t, c = map(int, input().split())
    edges[u-1][v-1] = [t, str(c)]
    edges[v-1][u-1] = [t, str(c)]

print(edges)
