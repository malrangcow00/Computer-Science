import sys
input = sys.stdin.readline

N = int(input())

positive = []
zero_negative = []

total = 0
for _ in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num <= 0:
        zero_negative.append(num)
    else:
        total += num

positive.sort()
zero_negative.sort()

N = len(positive)

if N % 2 == 0:
    for _ in range(0, N, 2):
        total += positive[_] * positive[_+1]
else:
    for _ in range(1, N, 2):
        total += positive[_] * positive[_+1]
    total += positive[0]

N = len(zero_negative)

if N % 2 == 0:
    for _ in range(0, N, 2):
        total += zero_negative[_] * zero_negative[_+1]
else:
    for _ in range(0, N-1, 2):
        total += zero_negative[_] * zero_negative[_+1]
    total += zero_negative[-1]

print(total)