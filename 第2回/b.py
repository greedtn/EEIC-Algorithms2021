Q = int(input())

is_prime = [True]*(2000000 + 1)

# エラトステネスの篩
is_prime[0] = False
is_prime[1] = False
now = 2
while now * now <= 2000000:
    if is_prime[now]:
        for i in range(now * 2, 2000000 + 1, now):
            is_prime[i] = False
    now += 1

ok = [0]
for i in range(1, 2000001):
    if i % 2 == 1 and is_prime[i] and is_prime[(i + 1) // 2]:
        ok.append(ok[i-1] + 1)
    else:
        ok.append(ok[i-1])

for i in range(Q):
    l, r = map(int, input().split())
    print(ok[r] - ok[l-1])

