N = int(input())
A = list(map(int, input().split()))

def shakersort(seq):
    right = len(seq) - 1
    left = 0

    swapped = 0
    while left < right:
        for i in range(left, right):
            if seq[i+1] < seq[i]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swapped = i
        right = swapped
        
        for i in range(right, left, -1):
            if seq[i-1] > seq[i]:
                seq[i], seq[i-1] = seq[i-1], seq[i]
                swapped = i
        left = swapped
    
    return seq

ans = shakersort(A)
for i in range(N):
    print(A[i])