import sys
string = sys.stdin.readline().rstrip()
string_set = set()
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        string_set.add(string[i:j])
print(len(string_set))