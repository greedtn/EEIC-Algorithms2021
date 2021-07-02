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
    
def kruskal(V, e_list, L, ng, indeg, ok_list):
    e_cost_sorted = [] #距離で整列された辺

    # ソートのために先頭の要素を距離にする
    for e in e_list:
        e_cost_sorted.append([e[2], e[0], e[1]])

    e_cost_sorted.sort()

    uf_tree = UnionFind(V)

    # 答え
    ans = 0

    # 使わなかったリスト
    unused_list = [[] for _ in range(V)]

    for e in e_cost_sorted:
        
        if (uf_tree.is_in_group(e[1], e[2]) == False) and  (L[e[1]] == False) and (L[e[2]] == False):
                uf_tree.unite(e[1], e[2])
                ans += e[0]

        else:
            unused_list[e[1]].append([e[2], e[0]])
            unused_list[e[2]].append([e[1], e[0]])
    
    ok_val = ok_list[0]
    for ng_val in ng:
        min_val = 100100100100
        for e in unused_list[ng_val]:
            if uf_tree.get_root(ok_val) == uf_tree.get_root(e[0]):
                min_val = min(min_val, e[1])
        if min_val == 100100100100:
            print("No")
            exit()
        else:
            ans += min_val

    ok = True
    for i in range(V):
        if (uf_tree.is_in_group(i, ok_val) == False) and ng_list[i] == False:
            ok = False
            break
    if ok:
        print("Yes")
        print(ans)
    else:
        print("No")

N, M = map(int, input().split())
indeg = [0] * N # 入次数を格納する配列
e_list = []
for _ in range(M):
    a, b, c = map(int, input().split())
    e_list.append([a-1, b-1, c])

ng_list = [False] * N
ok_list = []
L = int(input())
li = list(map(int, input().split()))
for l in li:
    ng_list[l-1] = True
ng = []
for i in range(N):
    if not ng_list[i]:
        ok_list.append(i)
    else:
        ng.append(i)
if N == 2 and L == 2:
    print("Yes")
    mn = 100100100100
    for e in e_list:
        mn = min(mn, e[2])
    print(mn)
    exit()
if L == N:
    print("No")
    exit()

kruskal(N, e_list, ng_list, ng, indeg, ok_list)
