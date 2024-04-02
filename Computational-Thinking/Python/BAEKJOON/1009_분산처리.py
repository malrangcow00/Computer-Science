import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
        continue
    nums = []
    i = 1
    N = 1
    while i <= b:
        N = N * a % 10
        if N not in nums:
            nums.append(N)
            i += 1
        else:
            break
    print(nums[(b-i+1)%len(nums)-1])