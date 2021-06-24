import heapq

def dijkstra_heap(V, e_list, s):
    """
    V : node数
    e_list : 隣接リスト
    s : 始点ノード
    """
    INF = 1001001001
    done = [False] * V
    dist = [INF] * V
    dist[s] = 0
    node_heap = [] # heap

    heapq.heappush(node_heap, [dist[s], s])

    while node_heap:
        tmp = heapq.heappop(node_heap)
        cur_node = tmp[1]

        if not done[cur_node]:
            for e in e_list[cur_node]:
                if dist[e[0]] > dist[cur_node] + e[1]:
                    dist[e[0]] = dist[cur_node] + e[1]
                    heapq.heappush(node_heap, [dist[e[0]], e[0]])
        done[cur_node] = True
    
    for d in dist:
        if d == INF:
            print("INF")
        else:
            print(d)

N, M, S = map(int, input().split())

edges = [[] for _ in range(N)]

for _ in range(M):
    a, b, d = map(int, input().split())
    edges[a].append([b, d])

dijkstra_heap(N, edges, S)