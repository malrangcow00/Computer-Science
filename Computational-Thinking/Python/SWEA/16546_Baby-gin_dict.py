import sys
sys.stdin = open('input/16546.txt', 'r')

T = int(input())
# for tc in range(1, T+1):
for tc in range(1, 2):
    cards = list(map(int, list(input())))
    temp_dict = {}
    for i in cards:
        if i not in temp_dict.keys():
            temp_dict[i] = 1
        else:
            temp_dict[i] += 1
        temp_dict = dict(sorted(temp_dict.items()))

    print(temp_dict)

    if 6 in temp_dict.values():
        result = 'true'
    elif 4

    elif 3

    elif 1

    else:

        #
        # temp_keys = list(temp_dict.keys())
        # for i in range(len(temp_keys)-2):
        #     if temp_keys[i]+2 == temp_keys[i+1]+1 == temp_keys[i+2]:
        #         result_1 = 'run!'
        #
        # if len(result_1) != 0 or len(result_2) != 0:
        #     if len(result_1) != 0 and len(result_2) != 0:
        #         print(f'#{tc} 0')
        #         break
        #     elif len(result_1) != 0:
        #         print(f'#{tc} 1')
        #         break
        #     else:
        #         print(f'#{tc} 2')
        #         break
        # else:
        #     if i == 6:
        #         print(f'#{tc} 0')