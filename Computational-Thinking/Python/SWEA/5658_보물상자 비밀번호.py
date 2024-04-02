import sys
sys.stdin = open('input/5658.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input().strip())
    M = N // 4
    scrt = []
    for _ in range(M):
        for i in range(4):
            scrt.append(int(''.join(arr[M*i:M*(i+1)]), 16))
        arr.insert(0, arr.pop())
    scrt = list(set(scrt))
    scrt.sort()
    print(f'#{tc} {scrt[-K]}')