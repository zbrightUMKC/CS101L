import math
import functools

def total(values):
    if len(values) > 0:
        return functools.reduce(lambda x, y: x + y, values)
    else:
        return 0

def average(values):
    if len(values) > 0:
        return total(values)/len(values)
    else:
        return math.nan

def median(values):
    list1 = sorted(values)
    if (len(values)) == 0:
        raise ValueError
    elif (len(values) % 2 == 0):
        median = (list1[(len(list1)//2)] + list1[(len(list1)//2) - 1]) / 2
        return median
    elif(len(values) % 1 == 0): 
        return list1[(len(list1)//2)]
    
