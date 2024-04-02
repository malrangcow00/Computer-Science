T = int(input())

cnt = T

for tc in range(T):
    word = input()
    skip = False
    for i in range(len(word)):
        if skip == True:
            break
        interval = False    
        for j in range(i+1, len(word)):
            if interval == True and word[i] == word[j]:
                cnt -= 1
                skip = True
                break
            if word[i] == word[j]:
                i = j
            else:
                interval = True
print(cnt)