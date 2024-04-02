import sys
sys.stdin = open('SWEA.input/18158.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    x1, y1, x2, y2 = map(int, input().split())
 
    for i in range(N):
        arr.append(list(map(int, input().split())))
 
    area = (y2-y1+1)*(x2-x1+1)
    chick = 0
    for j in range(N):
        if y2 >= j >= y1:
            for i in range(N):
                if x2 >= i >= x1:
                    chick += arr[i][j]
     
    mean = chick//area
    cnt = 0
 
    for j in range(N):
        if y2 >= j >= y1:
            for i in range(N):
                if x2 >= i >= x1:
                    if arr[i][j] > mean:
                        cnt += arr[i][j] - mean
                    else:
                        cnt -= arr[i][j] - mean
 
    print(f'#{tc} {cnt}')