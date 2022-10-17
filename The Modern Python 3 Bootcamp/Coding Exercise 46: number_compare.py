'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(f,p):
    if f > p: 
        return "First is greater"
    elif f < p:
        return "Second is greater"
    return "Numbers are equal"
