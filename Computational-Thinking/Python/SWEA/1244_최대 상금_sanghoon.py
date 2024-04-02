import sys
sys.stdin = open('input/1244.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, C = input().split()
    C = int(C)
    N_set = set([N])
    Newer = set()
    for _ in range(C):
        while N_set:
            s = list(N_set.pop())
            for i in range(len(N) - 1):
                for j in range(i+1, len(N)):
                    s[i], s[j] = s[j], s[i]
                    Newer.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        N_set, Newer = Newer, N_set

    res = max(map(int, N_set))
    print(f'#{tc} {res}')