import sys
input = sys.stdin.readline

# zero means ignore the current last number
K = int(input())
stack = []
for _ in range(K):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))