N, W = map(int, input().split())
vw = [list(map(int, input().split())) for _ in range(N)]
# vwをvでソート（昇順）
vw.sort()
INF = 10010010010
# DPテーブル
dp_b = [[[INF for _ in range(N+1)] for _ in range(W+1)] for _ in range(N+1)]
# 初期化
for i in range(N+1):
    for j in range(W+1):
        dp_b[i][j][0] = 0
for i in range(N):
    for j in range(W+1):
        for k in range(N+1):
            # 重さがj以下のとき
            if vw[i][1] <= j and k > 0:
                dp_b[i+1][j][k] = min(dp_b[i][j][k], dp_b[i][j-vw[i][1]][k-1] + vw[i][0])
            else:
                dp_b[i+1][j][k] = dp_b[i][j][k]
# 降順にソート
vw.reverse()
dp_a = [[[0 for _ in range(N+1)] for _ in range(W+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(W+1):
        for k in range(N+1):
            # 重さがj以下のとき
            if vw[i][1] <= j and k > 0:
                dp_a[i+1][j][k] = max(dp_a[i][j][k], dp_a[i][j-vw[i][1]][k-1] + vw[i][0])
            else:
                dp_a[i+1][j][k] = dp_a[i][j][k]

ans = -1
for i in range(N+1):
    for j in range(W+1):
        for k in range(1, N+1):
            ans = max(ans, dp_a[i][j][k] - dp_b[N-i][W-j][k-1])
print(ans)