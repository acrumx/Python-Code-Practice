# 5 kyu
# Link to the kata: https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def order_weight(strng):
    massa = [sum(int(i) for i in x) for x in strng.split(" ")]
    massas = list(zip(massa, strng.split()))  
    op = sorted(massas, key=lambda tup: (tup[0], tup[1]))
    return " ".join(o[1] for o in op)
order_weight("56 65 74 100 99 68 86 180 90")
