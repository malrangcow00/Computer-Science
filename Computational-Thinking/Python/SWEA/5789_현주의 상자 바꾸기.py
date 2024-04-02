import sys
sys.stdin = open('SWEA.test.txt', 'r')

# from sys import stdin
# stdin = open('SWEA.test.txt', 'r')
# 변수로 할당되어서 실행안됨

T = int(input())

for tc in range(1, T+1):
    N, Q =  map(int, input().split())
    arr = [0]*N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            arr[j] = i
    print(f'#{tc}', *arr)
    