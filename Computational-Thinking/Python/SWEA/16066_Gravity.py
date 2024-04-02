T = int(input())

for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    mx_cnt = 0
    cnt = 0
    for j in list(set(nums)):
        for k in nums:
            if j <= k:
                continue
            else:
                cnt += 1
        if mx_cnt < cnt-nums.index(j):
            mx_cnt = cnt-nums.index(j)
        cnt = 0
    print(f'#{i+1} {mx_cnt}')