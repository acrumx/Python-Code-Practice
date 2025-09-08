# Link to the kata: https://www.codewars.com/kata/54ff3102c1bad923760001f3/solutions/python
# 7 Kyu
import re 
def get_count(sentence):
    return len(re.findall(r'[aeiou]', sentence))
