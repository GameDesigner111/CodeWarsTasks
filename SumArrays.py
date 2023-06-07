def sum_array(a):
    sum = 0
    
    if a:
        for i in a:
            sum += i
        return sum
    else:
        return 0