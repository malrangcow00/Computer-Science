import sys
sys.stdin = open('input/5209.txt', 'r')

def DFS(depth):
    global mn
    global tmp
    if tmp > mn:
        return
    elif depth == N:
        mn = min(mn, tmp)
        return
    else:
        for factory in range(N):
            if not products[factory]:
                products[factory] = 1
                tmp += arr[depth][factory]
                DFS(depth+1)
                products[factory] = 0
                tmp -= arr[depth][factory]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    products = [0] * N
    mn = 9999999999999999999999
    tmp = 0
    DFS(0)
    print(f'#{tc} {mn}')