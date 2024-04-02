import sys
input = sys.stdin.readline

N = int(input())
alphabet = input().rstrip()
count = 1
result = "NO"

for _ in range(1, N):
    if abs(ord(alphabet[_]) - ord(alphabet[_ - 1])) == 1:
        count += 1
        if count == 5:
            result = "YES"
            break
    else:
        count = 1

print(result)