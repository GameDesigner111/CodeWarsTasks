def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        start = length // 2 - 1
        stop = start + 2
        return s[start:stop]
    else:
        index = length // 2
        return s[index]