#https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(s):
    for i in range(len(s)-1):
        if s[i] in "aeiou" or s[i] in "AEIOU":
            s = s.replace(s[i], "")
    return s