N = int(input())
big = N // 5
small = N // 3
packed = False
for j in range(0, small+1):
    if packed == True:
        break
    for i in range(big, -1, -1):
        if 5*i + 3*j == N:
            print(i+j)
            packed = True
            break
if packed == False:
    print(-1)