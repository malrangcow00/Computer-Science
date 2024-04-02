import sys
input = sys.stdin.readline

input()
prime_nums = list(map(int, input().split()))

if len(prime_nums) > 1:
    N = max(prime_nums) * min(prime_nums)
else:
    N = prime_nums[0]**2

print(N)