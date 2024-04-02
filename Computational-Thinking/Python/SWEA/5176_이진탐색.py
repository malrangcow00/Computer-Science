import sys
sys.stdin = open('input/5176.txt', 'r')

def tree(n):
    global start

    if n <= N:
        # LVR 왼쪽부터 끝까지 감
        tree(n * 2)         # 왼쪽노드
        arr[n] = start
        start += 1
        tree(n * 2 + 1)     # 오른쪽 노드

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0 for i in range(N + 1)]

    start = 1
    tree(start)

    print(f'#{tc} {arr[1]} {arr[N//2]}')