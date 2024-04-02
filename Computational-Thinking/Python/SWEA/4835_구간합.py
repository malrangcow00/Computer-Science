T = int(input())
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
 
    mn = mx = sum(nums[:M])
    for i in range(N-M+1):
        sum_nums = sum(nums[i:i+M])
        mn = min(mn, sum_nums)
        mx = max(mx, sum_nums)
 
    print(f'#{tc} {mx-mn}')