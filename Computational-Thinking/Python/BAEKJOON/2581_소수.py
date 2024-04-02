M = int(input())
N = int(input())

lst = []
for i in range(M, N+1):
    chk_lst=[]
    for j in range(1, i):
        if i % j == 0:
            chk_lst.append(j)
    if len(chk_lst) == 1:
        lst.append(i)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))