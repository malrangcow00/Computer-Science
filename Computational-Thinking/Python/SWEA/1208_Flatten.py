import sys
sys.stdin = open('SWEA.test.txt', 'r')

for i in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))
    for j in range(N):
        nums[nums.index(max(nums))] = max(nums) - 1
        nums[nums.index(min(nums))] = min(nums) + 1
        if max(nums) == min(nums):
            break
    print(f'#{i} {max(nums)-min(nums)}')