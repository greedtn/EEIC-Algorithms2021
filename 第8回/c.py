N = int(input())
c = list(map(int, input().split()))

dis_c = []
for i in range(N-1):
    if c[i] != c[i+1]:
        dis_c.append(c[i])

dp = [[-1 for _ in range(K+1)] for _ in range(N+1)]