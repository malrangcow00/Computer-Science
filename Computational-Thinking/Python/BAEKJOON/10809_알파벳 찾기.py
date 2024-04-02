alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string = input()
letters = []
for i in string:
    letters.append(i)

for i in range(len(alpha)):
    if alpha[i] in letters:
        print(string.index(alpha[i]), end=' ')
    else:
        print(-1, end=' ')