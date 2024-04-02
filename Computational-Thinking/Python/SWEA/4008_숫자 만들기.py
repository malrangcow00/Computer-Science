import sys
# sys.stdin = open('input/4008.txt', 'r')
sys.stdin = open('input/test.txt', 'r')

oper_trs = ['+', '-', '*', '/']
stack = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    oper_cnt = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    oper = []
    mx = -100000000
    mn = 100000000
    for _ in range(4):
        for i in range(oper_cnt[_]):
            oper.append(oper_trs[_])

    oper_comb = []

    def comb(i, arr):
        if i == len(arr):
            if arr not in oper_comb:
                oper_comb.append(arr)
        else:
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                comb(i+1, arr)
                arr[i], arr[j] = arr[j], arr[i]

    comb(0, oper)

    for _ in oper_comb:
        nums_temp = nums[:]
        while _:
            cal_oper = _.pop(0)
            cal_nums_1 = nums_temp.pop(0)
            cal_nums_2 = nums_temp.pop(0)
            if cal_oper == '+':
                nums_temp.insert(0, cal_nums_1 + cal_nums_2)
            elif cal_oper == '-':
                nums_temp.insert(0, cal_nums_1 - cal_nums_2)
            elif cal_oper == '*':
                nums_temp.insert(0, cal_nums_1 * cal_nums_2)
            else:
                nums_temp.insert(0, cal_nums_1 // cal_nums_2)
        mx = max(mx, nums_temp[0])
        mn = min(mn, nums_temp[0])

    # print(f'#{tc}', mx-mn)
    print(f'#{tc}', mx, mn)