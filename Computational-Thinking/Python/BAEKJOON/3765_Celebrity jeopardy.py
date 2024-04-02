import sys
input = sys.stdin.readline

result = []
while True:
    try:
        result.append(input().rstrip())
    except EOFError:
        break

print('\n'.join(result))
