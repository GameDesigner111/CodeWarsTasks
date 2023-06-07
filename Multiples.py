# https://www.codewars.com/kata/55a8a36703fe4c45ed00005b/train/python

def multiple(x):
    result = ""
    if x % 3 == 0:
        result += "Bang"
    if x % 5 == 0:
        result += "Boom"
    if result == "":
        result = "Miss"
    return result