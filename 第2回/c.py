N = int(input())
A = list(map(int, input().split()))
Q = int(input())
MOD = 998244353

zero_list = [False] * (N)

# s[i] : A1 ~ Ai までの積
s = [1]
for i in range(N):
    if A[i] == 0:
        s.append(s[i])
        zero_list[i] = True
    else:
        s.append(s[i] * A[i] % MOD)

zeros = [0]
for i in range(N):
    if zero_list[i]: zeros.append(zeros[i] + 1)
    else: zeros.append(zeros[i])

# s2[i] : s1 ~ si までの積
s2 = [1]
for i in range(N):
    s2.append(s2[i] * s[i+1] % MOD)

for i in range(Q):
    l, r = map(int, input().split())
    if zeros[l-1] != zeros[r-1]:
        print(0)
        continue
    ans = 1
    ans *= pow(s[r-1], r-l, MOD)
    if l != 1:
        ans *= s2[l-2]
    ans %= MOD
    ans *= pow(s2[r-2], MOD - 2, MOD)
    ans %= MOD
    print(ans)