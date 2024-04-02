T = int(input())

for tc in range(T):
    C = int(input())
    lst = []
    unit = [25, 10, 5, 1]
    for i in unit:
        lst.append(C // i)
        C = C % i
    print(*lst)

