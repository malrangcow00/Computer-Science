import sys
input = sys.stdin.readline

Z = int(input())
front = Z
len_cycle = 0
while True:
    back = front//10 + front%10
    if front >= 10:
        front %= 10
    if back >= 10:
        back %= 10
    len_cycle += 1
    front = front * 10 + back
    if front == Z:
        break
print(len_cycle)
