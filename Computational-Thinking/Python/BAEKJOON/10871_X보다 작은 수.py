N, X = map(int, input().split())
nums = list(map(int, input().split()))

nums_2 = []
for i in nums:
    if X > i:
        nums_2.append(i)
l = len(nums_2)
for j in range(l):
    print(nums_2[j], end=' ')