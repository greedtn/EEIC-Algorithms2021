

S = input()
N = int(input())

# ansを格納
ans = [None] * (N+1)
ans[0] = S

for i in range(N):
    plan = input().split()
    if int(plan[0]) == 1:
        ans[i+1] = plan[2]+ ans[int(plan[1])]
    else:
        ans[i+1] = ans[int(plan[1])][:-1]

Q = int(input())
for _ in range(Q):
    q = int(input())
    print(ans[q])

