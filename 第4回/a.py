MOD = 10 ** 6
hash = [None for _ in range(MOD)]

# 入出力
Q = int(input())
for i in range(Q):
    a, b = map(int, input().split())
    b_mod = b % MOD
    
    if a == 0:
        # 追加
        while hash[b_mod] is not None:
            # Noneを見つけるまで再帰を回す
            b_mod += 1
            b_mod %= MOD
        hash[b_mod] = b
        
    else:
        # 探索
        ok = False
        while hash[b_mod] is not None:
            if hash[b_mod] == b:
                ok = True
                break
            b_mod += 1
            b_mod %= MOD
        if ok:
            print("found")
        else:
            print("not found")
        

