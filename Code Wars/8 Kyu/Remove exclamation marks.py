# Link to the kata: https://www.codewars.com/kata/57a0885cbb9944e24c00008e
# 8 Kyu
def remove_exclamation_marks(s):
    return ''.join([x.replace('!', '') for x in s])
