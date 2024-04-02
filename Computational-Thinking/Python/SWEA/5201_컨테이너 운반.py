import sys
sys.stdin = open('input/5201.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wei = list(map(int, input().split()))
    cap = list(map(int, input().split()))
    wei.sort()
    cap.sort()
    total = 0
    t = cap.pop()
    while wei:
        w = wei.pop()
        if w > t:
            continue
        else:
            total += w
        if cap:
            t = cap.pop()
        else:
            break
    print(f'#{tc} {total}')