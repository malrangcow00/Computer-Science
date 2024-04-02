import sys
sys.stdin = open('input/5207.txt', 'r')

def BinarySearch(arr, left, right, target):
    global turn_left
    global turn_right
    mid = (left + right) // 2
    if mid >= len(arr):
        return False
    elif target == arr[mid]:
        return True
    elif target < arr[mid] and turn_left:
        return False
    elif target > arr[mid] and turn_right:
        return False
    elif target < arr[mid]:
        turn_left = True
        turn_right = False
        if BinarySearch(arr, left, mid-1, target):
            return True
    elif target > arr[mid]:
        turn_left = False
        turn_right = True
        if BinarySearch(arr, mid+1, right, target):
            return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for target in B:
        turn_left = False
        turn_right = False
        if BinarySearch(A, 0, N-1, target):
            cnt += 1
    print(f'#{tc} {cnt}')