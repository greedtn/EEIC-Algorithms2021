from collections import deque

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

visit = deque()

for e in es:
    visit.append((e-1, K))

while visit:
    v, step = visit.popleft()
    ok[v] = False
    if step == 0:
        continue

    for next_v in edges[v]:
        if ok[next_v]:
            visit.append((next_v, step-1))

for i in range(N):
    if ok[i]:
        print(i+1)