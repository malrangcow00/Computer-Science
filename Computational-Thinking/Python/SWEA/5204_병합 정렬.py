import sys
sys.stdin = open('input/5204.txt', 'r')

def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[-1] > right[-1]:
        cnt += 1

    result = [0] * (len(arr))
    idx = 0
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            result[idx] = right[right_idx]
            idx += 1
            right_idx += 1
        else:
            result[idx] = left[left_idx]
            idx += 1
            left_idx += 1

    while left_idx < len(left):
        result[idx] = left[left_idx]
        idx += 1
        left_idx += 1

    while right_idx < len(right):
        result[idx] = right[right_idx]
        idx += 1
        right_idx += 1

    return result

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc}', merge_sort(arr)[N//2], cnt)