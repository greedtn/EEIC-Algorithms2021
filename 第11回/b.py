from collections import deque
import heapq

def topoSort(V, E, edges):

    indeg = [0] * V # 入次数を格納する配列
    # 出力辺を保持する配列
    outedge = [[] for _ in range(V)]

    for v_from, v_to in edges:
        indeg[v_to] += 1
        outedge[v_from].append(v_to)

    # ソート済のノードを格納する配列
    # 最初は入次数0のものを入れておく
    sorted_g = list(v for v in range(V) if indeg[v] == 0)

    # 入次数0のノードを処理するためのheapq
    heap_q = []
    for val in sorted_g:
        heapq.heappush(heap_q, val)
    ans_list = []

    while heap_q:
        v = heapq.heappop(heap_q)
        ans_list.append(v)
        for node in outedge[v]:
            E -= 1
            indeg[node] -= 1
            if indeg[node] == 0:
                heapq.heappush(heap_q, node)

    if E != 0:
        print(-1)
    else:
        for ans in ans_list:
            print(ans)

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    edges.append([a, b])
topoSort(N, M, edges)