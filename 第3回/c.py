import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1)) # スタック領域を拡大
sys.setrecursionlimit(1000000) # 再帰回数の上限を拡大

S = input()
N = int(input())

ans = [None for _ in range(N+1)]
plan = [0]

for i in range(N):
    p = input().split()
    plan.append(p)

Q = int(input())
q_list = [False for _ in range(N+1)]
q_ = []
for _ in range(Q):
    q = int(input())
    q_list[q] = True
    q_.append(q)

def rec(p, q):
    if p[0] == "1":
        # 追加するときの操作
        if p[1] == "0":
            if q_list[q]:
                ans[q] = p[2] + S
                return ans[q]
            else:
                return p[2] + S
        else:
            if q_list[q]:
                ans[q] = p[2] + rec(plan[int(p[1])], int(p[1]))
                return ans[q]
            else:
                return p[2] + rec(plan[int(p[1])], int(p[1]))
    else:
        # 削除するときの操作
        if p[1] == "0":
            if q_list[q]:
                ans[q] = S[:-1]
                return ans[q]
            else:
                return S[:-1]
        else:
            old = rec(plan[int(p[1])], int(p[1]))
            if q_list[q]:
                ans[q] = old[:-1]
                return ans[q]
            else:
                return old[:-1]

for q in q_:
    if ans[q] != None:
        print(ans[q])
    else:
        print(rec(plan[q], q))
