from collections import Counter


def solution(a, b, c, d):
    freq = Counter([a, b, c, d])
    values, counts = zip(*freq.items())
    if len(freq) == 1:
        return 1111 * a
    elif 3 in counts:
        triple = values[counts.index(3)]
        single = values[counts.index(1)]
        return (10 * triple + single) ** 2
    elif 2 in counts and len(freq) == 2:
        pairs = [value for value, count in freq.items() if count == 2]
        return (pairs[0] + pairs[1]) * abs(pairs[0] - pairs[1])
    elif 2 in counts:
        singles = [value for value, count in freq.items() if count == 1]
        return singles[0] * singles[1]
    else:
        return min(a, b, c, d)
