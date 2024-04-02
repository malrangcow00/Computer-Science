import sys
sys.stdin = open('input/2871.txt', 'r')

def subset(N, i, s):
    global cnt
    if i == N:
        if s == K:
            cnt += 1
        return
    result.append(nums[i])
    subset(N, i + 1, s + nums[i])
    result.pop()
    subset(N, i + 1, s)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    result = []
    cnt = 0
    subset(N, 0, 0)
    print(f'#{tc} {cnt}')