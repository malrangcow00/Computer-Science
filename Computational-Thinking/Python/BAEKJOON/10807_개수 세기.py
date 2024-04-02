N = input()
numbers = list(map(int, input().split()))
num = int(input())
cnt = 0
for i in numbers:
    if num == i:
        cnt += 1
print(cnt)