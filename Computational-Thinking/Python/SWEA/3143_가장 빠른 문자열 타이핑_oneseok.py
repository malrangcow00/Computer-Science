import sys
sys.stdin = open('SWEA.input/3143.txt', 'r')

def bm(t, p):
 
    ips = [len(p) for i in range(256)]
    res = 0
    i = 1
    for a in p[::-1][1:]:
        if ips[ord(a)] == len(p):
            ips[ord(a)] = i
        i += 1
    i = len(p)-1
    j = len(p)-1
    while i < len(t):
        if t[i] == p[j]:
            is_cheched = True
            for k in range(0, len(p)):
                if t[i-k] != p[j-k]:
                    is_cheched = False
                    break
            if is_cheched:
                res += 1
                j = len(p) - 1
                i += len(p)
            else:
                j = len(p) - 1
                i += ips[ord(t[i])]
        else:
            j = len(p)-1
            i += ips[ord(t[i])]
    return res
 
 
T = int(input())
for tc in range(1, T+1):
    str1, str2 = input().split()
    ans = bm(str1, str2)
    ans += len(str1) - ans * len(str2)
    print(f'#{tc} {ans}')