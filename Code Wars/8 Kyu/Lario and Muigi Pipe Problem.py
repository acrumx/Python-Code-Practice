# https://www.codewars.com/kata/56b29582461215098d00000f/train/python
# 8 Kyu
def pipe_fix(nums):
    a1 = nums[0]
    a2 = nums[-1]
    newli = []
    for i in range(a1,a2+1): 
        newli.append(i)
    return newli
