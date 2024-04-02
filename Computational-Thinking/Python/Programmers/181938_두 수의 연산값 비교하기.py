def solution(a, b):
    ab = int(str(a)+ str(b))
    if ab > 2*a*b:
        return ab
    else:
        return 2*a*b