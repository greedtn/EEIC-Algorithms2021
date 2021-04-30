N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    v = int(input())
    left = 0
    right = N - 1
    if A[right] <= v:
        print("not exist")
    else:
        while right - left > 1:
            m = (left + right) // 2
            if A[m] <= v:
                left = m
            else:
                right = m
        if A[right] == v:
            print(A[right+1])
        else:
            print(A[right])

