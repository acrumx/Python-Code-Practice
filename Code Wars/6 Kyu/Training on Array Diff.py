# Link to Kata: https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
# 6 kyu 

# Initial solution, which did not pass test cases due to the fact that: 
# It does not remove all instances of  the specified list item from the specified list, out of the target list.
# With that being said, had to use a list comprehension which is one of multiple ways that it can be solved.

# def array_diff(a, b):    
#     for i in b:
#         if i in a:
#             a.remove(i)
#     return a


# Working Solution below (Passes all test cases):

def array_diff(a, b):
    return [i for i in a if i not in b]
