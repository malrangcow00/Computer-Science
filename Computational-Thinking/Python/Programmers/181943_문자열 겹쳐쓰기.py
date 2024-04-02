def solution(my_string, overwrite_string, s):
    oldstr = len(my_string)
    newstr = len(overwrite_string)
    list_str = list(my_string)
    for i in range(newstr):
        list_str[s] = overwrite_string[i]
        s += 1
    return ''.join(list_str)