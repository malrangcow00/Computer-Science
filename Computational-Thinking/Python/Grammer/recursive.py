# for i in range(1,4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             print(i, j, k)

nums = []
def recur(depth, N):
    global nums
    if depth == N+1:
        print(nums)
        return
    for i in range(1, N+1):
        nums.append(i)
        recur(depth + 1, N)
        nums.pop()
recur(1, 3)