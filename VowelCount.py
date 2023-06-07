# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    return len([i for i in sentence if i.lower() in "aeiou"])
    
