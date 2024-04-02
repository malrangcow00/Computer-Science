def generate_all_subsets(nums):
    n = len(nums)
    total_subsets = 2 ** n
    all_subsets = []

    for i in range(total_subsets):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(nums[j])
        all_subsets.append(subset)

    return all_subsets

# Test the function
nums = [1, 2, 3]
subsets = generate_all_subsets(nums)
print(subsets)

# N개의 부분집합의 원소의 합이 K인 경우
# 공집합은 N개에 포함시킬 수 없다 ?
# 검증해보기

# sum_factors = []
# for i in subsets:
#     sum_factors.append(sum(i))

# print(sum_factors)

# nums = [1, 2, 3]
# for i in range(2 ** len(nums)):
    # pass