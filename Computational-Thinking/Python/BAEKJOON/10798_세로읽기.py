lst = []
for i in range(5):
    lst.append(list(input()))
len_lst = []
for i in lst:
    len_lst.append(len(i))
for i in range(max(len_lst)): # 최대 길이
    for j in range(5):
        if len(lst[j]) != 0:
            print(lst[j].pop(0), end='')
print()