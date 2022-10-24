# Link to the kata: https://www.codewars.com/kata/55f2b110f61eb01779000053/

def square_sum(numbers):
    p = 0
    for num in numbers:
        p = (num ** 2) + p
    return p
