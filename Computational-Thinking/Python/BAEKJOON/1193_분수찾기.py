X = int(input())

i = 0
total = 0

while total < X:
    i += 1
    total += i

sum = i + 1

if i % 2 == 1:
    print(f'{total-X+1}/{sum-total+X-1}')
else:
    print(f'{sum-total+X-1}/{total-X+1}')