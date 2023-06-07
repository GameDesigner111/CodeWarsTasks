def printer_error(s):
    # your code
    normalLetters = 0
    for i in s:
        if ord("a") <= ord(i) <= ord("m") or ord("A") <= ord(i) <= ord("M") :
            normalLetters += 1
    errors = len(s) - normalLetters
    return str(errors)+'/'+str(len(s))