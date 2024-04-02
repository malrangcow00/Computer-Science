wstr = 'askdawdadkwolkdlasdlsjasasasjdiwjdlwadkljasldkjlwijdadjlsiaassdwjildajljwlidjlasjkdjisasasawdasas'
word = 'asd'

def JP(wstr, word):
    cnt = 0
    for i in range(len(wstr)):
        if word[0] == wstr[i]:
            for j in range(len(word)):
                if i+j < len(wstr) and word[j] == wstr[i+j]:
                    if j == len(word)-1:
                        cnt += 1
                else:
                    break
    return cnt


print(JP(wstr, word))