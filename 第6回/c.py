N = int(input())
A = list(map(int, input().split()))

dict = {}
# keyはA[i]の値, valueは配列になっていて, A[i]=keyとなるindexを格納
for idx, val in enumerate(A):
    dict.setdefault(val, []).append(idx)

# 辞書をkeyでソートする
list = sorted(dict.items(), key=lambda x: x[0])
dict.clear()
dict.update(list)

# 今までの合計距離
d = 0
# 今いる地点(0 ~ N-1)
now = 0

# 値の小さい方から見ていく
for key, vec in dict.items():
    # 同じA[i]を取るものの中で, nowから最も遠いもの
    x = max(x if x >= now else x + N for x in vec)
    # now ~ x まで移動する
    d += (x - now)
    # now は N以上にならないので, %Nする
    now = x % N

# 答えはdになる
print(d)



