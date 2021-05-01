N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ABC = A + B + C
ABC.sort()


def binary_search(list, value):

    left = 0
    right = N-1
    while right - left > 1:
        m = (left + right) // 2
        if list[m] <= value:
            left = m
        else:
            right = m
    if list[left] == value:
        return [left]
    elif list[right] == value:
        return [right]
    else:
        if left == 0 and list[0] > value:
            left = -1
            right = 0
        if right == N-1 and list[N-1] < value:
            left = N-1
            right = N
        return [left, right]



# これがK以上になるような最初の中央値が答えになる
sum = 0

for i in range(1, 3*N - 1):
    # print("中央値の値", ABC[i])
    a = binary_search(A, ABC[i])
    b = binary_search(B, ABC[i])
    c = binary_search(C, ABC[i])
    # print(a, b, c)
    if len(a) == 1:
        sum += (b[0] + 1) * (N - c[1]) + (N - b[1]) * (c[0] + 1)
    if len(b) == 1:
        sum += (c[0] + 1) * (N - a[1]) + (N - c[1]) * (a[0] + 1)
    if len(c) == 1:
        sum += (a[0] + 1) * (N - b[1]) + (N - a[1]) * (b[0] + 1)
    # print("現在の合計値", sum)
    if sum >= K:
        print(ABC[i])
        break


