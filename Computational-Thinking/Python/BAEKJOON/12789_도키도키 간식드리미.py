from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = deque(map(int, input().split()))
cnt = 1
stack = deque()
while True:
    if stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1
    elif arr and arr[0] == cnt:
        arr.popleft()
        cnt += 1
    elif arr and arr[0] != cnt:
        stack.append(arr.popleft())
    else:
        break
if arr or stack:
    print('Sad')
else:
    print('Nice')