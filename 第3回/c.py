import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1)) # スタック領域を拡大
sys.setrecursionlimit(1000000) # 再帰回数の上限を拡大

S = input()
N = int(input())

plan = [0]

for i in range(N):
    p = input().split()
    plan.append(p)
    # print(plan)

def rec(p):
    if p[0] == "1":
        # 追加するときの操作
        if p[1] == "0":
            return p[2] + S
        else:
            return p[2] + rec(plan[int(p[1])])
    else:
        # 削除するときの操作
        if p[1] == "0":
            return S[:-1]
        else:
            old = rec(plan[int(p[1])])
            return old[:-1]

Q = int(input())
for _ in range(Q):
    q = int(input())
    print(rec(plan[q]))
