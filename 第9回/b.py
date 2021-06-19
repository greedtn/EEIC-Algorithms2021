from collections import deque

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

INF = 10 ** 6

A = [input() for _ in range(H)]
ans = [[INF for _ in range(W)] for _ in range(H)]
ans[sy-1][sx-1] = 0

qx = deque()
qx.append(sx-1)
qy = deque()
qy.append(sy-1)

vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]

while qx:
    x = qx.popleft()
    y = qy.popleft()

    for i in range(4):
        nx = x + vx[i]
        ny = y + vy[i]
        if 0 <= nx and nx <= W-1 and 0 <= ny and ny <= H-1:
            now = ans[y][x]
            next = ans[ny][nx]
            # 後半のif文がないと無限ループになる
            if A[ny][nx] == "." and (next == INF or now + 1 < next):
                ans[ny][nx] = now + 1
                qx.append(nx)
                qy.append(ny)
print(ans[gy-1][gx-1])