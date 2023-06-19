#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def accum(s):
    result = ""
    for i in range(len(s)):
        result += s[i].upper()+s[i].lower()*i+"-"
    return result.rstrip("-")