def solve(a, b):
    base = 1007
    h = 10**9 + 7
    al = len(a)
    bl = len(b)
    if al > bl:
        return False

    t = 1
    for i in range(al):
        t *= base
        t %= h
    
    ah = 0
    bh = 0
    for i in range(al):
        ah = ah * base + ord(a[i])
        ah %= h
    for i in range(al):
        bh = bh * base + ord(b[i])
        bh %= h
    for i in range(bl - al + 1):
        if ah == bh:
            print(i)
        if i + al < bl:
            bh = bh * base + ord(b[i+al]) - ord(b[i]) * t
            bh %= h

    return False

S = input()
T = input()

solve(T, S)