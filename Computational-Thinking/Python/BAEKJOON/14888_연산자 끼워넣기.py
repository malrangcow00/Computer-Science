import sys
input = sys.stdin.readline

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)

N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

maximum = -1E9
minimum = 1E9

dfs(1, nums[0], opers[0], opers[1], opers[2], opers[3])
print(maximum)
print(minimum)