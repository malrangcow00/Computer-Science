import sys
input = sys.stdin.readline

N, M = map(int, input().split())
clover = []
for _ in range(N):
    clover.append(list(map(int, input().split())))
command_list = list(input().rstrip())

coordinate = [0, 0]

for command in command_list:
    if command == 'R':
        while True:
            coordinate[0] += 1
            if coordinate in clover:
                break
    elif command == 'L':
        while True:
            coordinate[0] -= 1
            if coordinate in clover:
                break
    elif command == 'U':
        while True:
            coordinate[1] += 1
            if coordinate in clover:
                break
    elif command == 'D':
        while True:
            coordinate[1] -= 1
            if coordinate in clover:
                break
print(*coordinate)