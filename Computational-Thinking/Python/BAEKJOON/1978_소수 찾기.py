N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for _ in range(N):
    num = nums[_]
    lst = []
    for i in range(1, num+1):
        if num % i == 0:
            lst.append(i)
    if len(lst) == 2:
        cnt += 1
print(cnt)