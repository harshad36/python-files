'''
built in modules
================

                         modules
                            |
                --------------------------
               |            |             |
             Functions    Constants    Classes

In order to use math module in the python file. Then
there is s need to import that module

step1: import module
step2: use that module
'''


'''
import math
#factorial
r=math.factorial(4)
print("Factorial of number is:",r)
'''


#import math as m
#ceil() and floor()

#ceil()
'''
15.5=>15 to 16 =>16
15.3=>15 to 16 =>16
15.9=>15 to 16 =>16
'''
'''
print("ceil")
print(m.ceil(15.4))
print(m.ceil(15.8))
print(m.ceil(15.1))
'''

#floor()
'''
15.5=>15 to 16 =>15
15.3=>15 to 16 =>15
15.9=>15 to 16 =>15
'''
'''
print("floor")
print(m.floor(15.4))
print(m.floor(15.8))
print(m.floor(15.1))
'''

#import specific functionality from module
from math import  factorial,sqrt

r=factorial(6)
print("factorial is:",r)

sroot=sqrt(25)
print("square root is:",sroot)
