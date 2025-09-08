# Link to the kata:
# 8 kyu
def simple_multiplication(number) :
    alp = lambda number: number*8 if (number % 2 == 0) else (number*9)
    return alp(number)
