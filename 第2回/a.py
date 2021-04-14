N, K = map(int, input().split())
MOD = 10 ** 9 + 7

# 繰り返し自乗法
def power(x, n):
    if n == 0:
        return 1
    tmp = power(x * x % MOD, n // 2)
    if n % 2 == 1:
        tmp = tmp * x % MOD
    return tmp

# nCk
def nCk(n, k):
    res = 1
    for i in range(n - k + 1, n+1):
        res *= i
        res %= MOD
    x = 1
    for i in range(1, k + 1):
        x *= i
        x %= MOD
    res *= power(x, MOD - 2)
    return res % MOD

print(nCk(N, K))