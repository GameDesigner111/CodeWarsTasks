#https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
def sum_two_smallest_numbers(numbers):
    ls = []
    a = min(numbers)
    numbers.remove(a)
    ls.append(a)
    a = min(numbers)
    ls.append(a)
    return sum(ls)