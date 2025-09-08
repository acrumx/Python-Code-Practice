# Link to the kata: https://www.codewars.com/kata/56b1f01c247c01db92000076/solutions/python
# 8 Kyu
def double_char(s):
    total = []
    for i in s: 
        total += str(i * 2)
    total2 = ''.join(total)
    return total2 
