N = int(input())
A = list(map(int, input().split()))
# seqを直接編集して, ソートする関数
def qsort(seq, left, right):
    if left >= right:
        return
    pivot = seq[(left+right) // 2]
    # カーソルを用意
    l = left
    r = right
    while True:
        while seq[l] < pivot:
            l += 1
        while seq[r] > pivot:
            r -= 1
        if r <= l:
            break
        seq[l], seq[r] = seq[r], seq[l]
        l += 1
        r -= 1
    qsort(seq, left, l-1)
    qsort(seq, r+1, right)

qsort(A, 0, N-1)
for i in range(N):
    print(A[i])