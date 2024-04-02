import sys
sys.stdin = open('SWEA.input/1234.txt', 'r')

for tc in range(1, 11):
    stack = []
    N, nums_str = map(str, input().split())
    nums_str = list(nums_str)
    for i in nums_str:
        if stack == [] or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()
    nums = ''.join(stack)
    print(f'#{tc} {nums}')
    