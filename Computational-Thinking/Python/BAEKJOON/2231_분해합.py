N = int(input())
M = N//2
decomposition = M
while M < N:
    decomposition = M
    M_list = list(str(M))
    for i in M_list:
        decomposition += int(i)
    if decomposition == N:
        print(M)
        break
    else:
        M += 1
# 분해합이 N보다 커진 경우는 물론 M이 N보다 크지만 decomposition이 N이상의 크기에 도달하지 못한 경우(N = 1인 경우)도 포함해 주어야 한다.
if decomposition != N:
    print(0)