def func(S, N):
    R = [0 for _ in range(N)]
    i = 0
    j = 0
    while i < N:
        while i-j >= 0 and i+j < N and S[i-j] == S[i+j]:
            j += 1
        R[i] = j
        k = 1
        while i-k >= 0 and k + R[i-k] < j:
            R[i+k] = R[i-k]
            k += 1
        i += k
        j -= k
    return R

S = input()
N = len(S)

ans = 0
R1 = func(S, N)
for v in R1:
    ans += v
S_ = ""
for i in range(N-1):
    S_ += S[i]
    S_ += '$'
S_ += S[N-1]

R2 = func(S_, 2*N-1)
for i in range(2*N-1):
    if i % 2 == 1:
        ans += R2[i]//2
print(ans)