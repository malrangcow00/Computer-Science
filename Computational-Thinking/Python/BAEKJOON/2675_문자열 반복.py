T = int(input())

for i in range(T):
    num_str = input()
    for k in num_str[2:]:
        for j in range(int(num_str[0])):
            print(k, end='')
    print()