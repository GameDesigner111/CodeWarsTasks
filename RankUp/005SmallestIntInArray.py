#https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python

def find_smallest_int(arr):
    min = 10000000
    for i in arr:
        if i < min:
            min = i
    return min
