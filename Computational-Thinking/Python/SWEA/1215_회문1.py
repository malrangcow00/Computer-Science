import sys
sys.stdin = open('input/1215.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(input()) for i in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                cnt += 1
    for i in range(8):
        for j in range(8):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')


    