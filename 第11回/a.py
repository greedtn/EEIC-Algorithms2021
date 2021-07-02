from typing import Union


class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [0 for _ in range(n)] # 各木の高さ
    
    def get_root(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.get_root(self.parent[i])
            return self.parent[i]
        
    def unite(self, i, j):
        root_i = self.get_root(i)
        root_j = self.get_root(j)
        if root_i != root_j:
            if self.height[root_i] < self.height[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                if self.height[root_i] == self.height[root_j]:
                    self.height[root_i] += 1
    
    def is_in_group(self, i, j):
        if self.get_root(i) == self.get_root(j):
            return True
        else:
            return False
    
def kruskal(V, e_list):
    e_cost_sorted = [] #距離で整列された辺

    # ソートのために先頭の要素を距離にする
    for e in e_list:
        e_cost_sorted.append([e[2], e[0], e[1]])

    e_cost_sorted.sort()

    uf_tree = UnionFind(V)

    # 答え
    ans = 0

    for e in e_cost_sorted:
        # print(uf_tree.parent)
        # print(e[1], e[2], uf_tree.is_in_group(e[1], e[2]))
        if not uf_tree.is_in_group(e[1], e[2]):
            uf_tree.unite(e[1], e[2])
            ans += e[0]
            # print(ans)
    
    print(ans)

N, M = map(int, input().split())
e_list = []
for _ in range(M):
    a, b, d = map(int, input().split())
    e_list.append([a, b, d])

kruskal(N, e_list)
