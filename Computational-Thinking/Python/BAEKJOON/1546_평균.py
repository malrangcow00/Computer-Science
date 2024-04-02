T = int(input())

sub_list = list(map(int, input().split()))

print(sum(sub_list)/max(sub_list)*100/T)