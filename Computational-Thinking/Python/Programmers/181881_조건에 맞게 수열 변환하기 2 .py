def solution(arr):
    l = len(arr)
    check_arr = [True] * l
    cnt = -1
    while True:
        flag = True
        cnt += 1
        for i in range(l):
            if check_arr[i]:
                if arr[i] >= 50 and arr[i] % 2 == 0:
                    arr[i] /= 2
                    flag = False
                elif arr[i] < 50 and arr[i] % 2 == 1:
                    arr[i] = arr[i] * 2 + 1
                    flag = False
                else:
                    check_arr[i] = False
        if flag:
            break
    return cnt