word = input()

make_lower = word.lower()

dict = {}

for i in make_lower:
    if i not in dict:
        dict[i] = 0
    dict[i] += 1

cnt = 0
for i in list(dict.values()):
    if i == max(dict.values()):
        cnt += 1

rev_dict = {value: key for key, value in dict.items()}
find_max_key = rev_dict.get(max(dict.values()))

if cnt > 1:
    print("?")
else:
    print(find_max_key.upper())