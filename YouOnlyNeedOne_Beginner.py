#https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python

#NotCorrect
def check(seq, elem):
    nE = False
    for i in range(len(seq)-1):
        if isinstance(seq[i], int) == True:
            nE = True
            
        else:
            nE = False
            break
        
    if nE == True:          
        for i in range(len(seq)-1):
            if elem == seq[i]:
                return True
            else:
                return False
                
    if nE == False:
        for i in range(len(seq)):
            if str(elem) in str(seq[i]):
                return True
            else:
                return False

#Correct
def check(seq, elem):
    if elem in seq: 
        return True
    else:
        return False