import sys
sys.stdin = open('input/1223.txt', 'r')

for tc in range(1, 11):
    input()
    arr = input()
    nums = []
    opers = []
    for _ in arr:
        if _.isdigit() and opers != [] and opers[-1] == '*':
            nums.append(nums.pop() * int(_))
        elif _.isdigit():
            nums.append(int(_))
        else:
            opers.append(_)
    print(f'#{tc} {sum(nums)}')