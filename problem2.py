#!python3
"""
Create a function that finds the missing side in a right triangle.
3 input parameters:
float: one side
float: another side
boolean: indicates whether one of the sides is the hypotenuse

return: float length of the missing side

Sample assertions:
assert hypotenuse(12,5,False) == 13
assert hypotenuse(5,3,True) == 4
(2 points)
"""

def hypotenuse (a,b,c):
    if c == True:
        x = sqrt(a**2 + b**2)
        return x 
    elif c == False:
        if a > b:
            x = math.sqrt(a**2 - b**2)
            return x
    elif c == False:
        if b > a:
            x = math.sqrt(b**2 - a**2)
            return x