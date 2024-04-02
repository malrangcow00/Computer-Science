import sys
sys.stdin = open('SWEA.test.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = input()
    cnt = 0
    pre_cnt = 0
    for i in range(N):
        if i == N-1:
            if int(C[i]) == 1:
                cnt += 1
            if pre_cnt > cnt:
                cnt = pre_cnt
            print(f'#{tc} {cnt}')
            break
        elif int(C[i]) == 0:
            if pre_cnt != 0:
                if pre_cnt < cnt:
                    pre_cnt = cnt
            else:
                pre_cnt = cnt
                cnt = 0
        else:
            cnt += 1