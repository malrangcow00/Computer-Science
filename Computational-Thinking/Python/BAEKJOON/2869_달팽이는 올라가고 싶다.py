A, B, V = map(int, input().split())

distance = A

if (V-A)%(A-B) == 0:
    day = (V-A)//(A-B)+1    
else:
    day = (V-A)//(A-B)+2

print(day)