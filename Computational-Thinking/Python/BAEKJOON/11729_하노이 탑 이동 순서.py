import sys
input = sys.stdin.readline

def hanoi(N, source, auxiliary, target):
    if N == 1:
        ways.append((source, target))
        return 1
    else:
        # Move N-1 disks from source to auxiliary using target as auxiliary peg
        count1 = hanoi(N-1, source, target, auxiliary)

        # Move the N-th disk from source to target
        ways.append((source, target))

        # Move the N-1 disks from auxiliary to target using source as auxiliary peg
        count2 = hanoi(N-1, auxiliary, source, target)

        return count1 + count2 + 1

ways = []
# cnt = 2**N-1
print(hanoi(int(input()), 1, 2, 3))
for way in ways:
    print(*way)