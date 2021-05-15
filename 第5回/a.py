def create_table(pattern):
    table = [0] * (len(pattern) + 1)
    table[0] = -1
    i, j = 0, 1

    while j < len(pattern):
        matched = pattern[i] == pattern[j]

        if not matched and i > 0:
            i = table[i]
        else:
            if matched:
                i += 1
            j += 1
            table[j] = i

    return table
 
def kmp(text, pattern):
    skip = create_table(pattern)
    t_len = len(text)
    p_len = len(pattern)
    t_i = 0
    p_i = 0
    while t_i < t_len and p_i < p_len:
        if text[t_i] == pattern[p_i]:
            t_i += 1
            p_i += 1
        elif p_i == 0:
            t_i += 1
        else:
            p_i = skip[p_i]
    
    # 照合が完了した場合
    if p_i == len(pattern):
        print(t_i - p_i)
    
    # 見つからなかった場合
    else:
        return print(-1)
 

S = input()
T = input()

# そもそもTの方が長い時は絶対に一致しない
if len(S) < len(T):
    print(-1)
    exit()

ans = kmp(S, T)