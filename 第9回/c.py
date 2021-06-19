import sys
import resource

sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))

N, M = map(int, input().split())

edges = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)

E = int(input())

# -1 することを忘れない
es = list(map(int, input().split()))

K = int(input())

ok = [True] * N

def dfs(edges, v, step):
    if step == 0:
        return 0
        
    ok[v] = False
    
    for next_v in edges[v]:
        dfs(edges, next_v, step-1)


for e in es:
    ok[e-1] = False

    for next_e in edges[e-1]:
        dfs(edges, next_e, K)

for i in range(N):
    if ok[i]:
        print(i+1)