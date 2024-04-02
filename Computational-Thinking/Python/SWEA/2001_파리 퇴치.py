import sys
sys.stdin = open('input/2001.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    sum_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_sum = 0
            
            for k in range(M):
                for l in range(M):
                    temp_sum += arr[i+k][j+l]
            
            sum_fly = max(temp_sum, sum_fly)

    print(f'#{tc} {sum_fly}')