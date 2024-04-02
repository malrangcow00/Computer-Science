import sys
sys.stdin = open('SWEA.test.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1
    pre_cnt = 1
    for i in range(N):
        if i == N-1:
            if pre_cnt > cnt:
                cnt = pre_cnt
            print(f'#{tc} {cnt}')
            break
        elif C[i]+1 != C[i+1]:
            if pre_cnt != 1:
                if pre_cnt < cnt:
                    pre_cnt = cnt
            else:
                pre_cnt = cnt
                cnt = 1
        else:
            cnt += 1