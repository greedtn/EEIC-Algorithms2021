import sys
import resource

sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))

N, M, S, T = map(int, input().split())
S -= 1
T -= 1

edges = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

done = [False] * N
done[S] = True

def dfs(edges, v):
    done[v] = True

    for next_v in edges[v]:
        if (next_v == T):
            print("Yes")
            exit()
        if (done[next_v]):
            continue
        dfs(edges, next_v)

dfs(edges, S)

print("No")

