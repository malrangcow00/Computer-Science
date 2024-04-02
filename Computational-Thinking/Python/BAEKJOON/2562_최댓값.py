import sys

numbers = []

for line in sys.stdin.readlines():
    num = line.strip()
    numbers.append(int(num))

max_num = max(numbers)
max_index = numbers.index(max_num) + 1

print(max_num)
print(max_index)
