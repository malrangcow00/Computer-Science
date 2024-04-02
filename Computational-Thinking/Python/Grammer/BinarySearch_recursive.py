# 이진 검색 - 재귀호출 활용
def BinarySearch(low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySearch(low, mid - 1, target)
    else:
        return BinarySearch(mid + 1, high, target)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr.sort()
N = len(arr)
print(BinarySearch(0, N-1, 10))