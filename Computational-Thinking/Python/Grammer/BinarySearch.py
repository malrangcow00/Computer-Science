def BinarySearch(target):
    low = 0
    high = len(arr) - 1

    # low > high가 되면 탐색 실패
    while low <= high:
        mid = (low + high) // 2

        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            return mid

        # 2. 가운데 값이 정답보다 작은 경우
        elif arr[mid] < target:
            low = mid + 1

        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = mid - 1

    return -1


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr.sort()
print(BinarySearch(10))