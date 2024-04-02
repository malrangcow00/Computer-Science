N = int(input())
nums = list(map(int, input().split()))

nums_keys = list(set(nums))

nums_keys.sort()

nums_dict = {}
for _ in range(len(nums_keys)):
    nums_dict[nums_keys[_]] = _

for _ in nums:
    print(nums_dict[_], end=' ')