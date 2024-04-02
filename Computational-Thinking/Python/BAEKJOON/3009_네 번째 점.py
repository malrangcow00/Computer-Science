x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    if x_list == [] or x not in x_list:
        x_list.append(x)
    else:
        x_list.pop(x_list.index(x))

    if y_list == [] or y not in y_list:
        y_list.append(y)
    else:
        y_list.pop(y_list.index(y))
        
print(x_list[0], y_list[0])