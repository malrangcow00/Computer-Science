import sys
sys.stdin = open('input/5203.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    card_list = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    for i in range(12):
        if i % 2 == 0:
            player_1.append(card_list[i])
        else:
            player_2.append(card_list[i])
    result_1 = ''
    result_2 = ''

    for i in range(3, 7):
        temp_dict = {}
        for j in player_1[:i]:
            if j not in temp_dict.keys():
                temp_dict[j] = 0
            temp_dict[j] += 1
        temp_dict = dict(sorted(temp_dict.items()))
        if 3 in temp_dict.values():
            result_1 = 'triplet'
        temp_keys = list(temp_dict.keys())
        for j in range(len(temp_keys)-2):
            if temp_keys[j]+2 == temp_keys[j+1]+1 == temp_keys[j+2]:
                result_1 = 'run!'

        temp_dict = {}
        for j in player_2[:i]:
            if j not in temp_dict.keys():
                temp_dict[j] = 0
            temp_dict[j] += 1
        temp_dict = dict(sorted(temp_dict.items()))
        if 3 in temp_dict.values():
            result_2 = 'triplet'
        temp_keys = list(temp_dict.keys())
        for j in range(len(temp_keys)-2):
            if temp_keys[j]+2 == temp_keys[j+1]+1 == temp_keys[j+2]:
                result_2 = 'run!'

        if len(result_1) != 0 or len(result_2) != 0:
            if len(result_1) != 0 and len(result_2) != 0:
                print(f'#{tc} 0')
                break
            elif len(result_1) != 0:
                print(f'#{tc} 1')
                break
            else:
                print(f'#{tc} 2')
                break
        else:
            if i == 6:
                print(f'#{tc} 0')