X = int(input())
N = int(input())

bill = 0

for i in range(N):
    a, b = map(int, input().split())
    bill += a*b

if bill == X:
    print('Yes')
else:
    print('No')