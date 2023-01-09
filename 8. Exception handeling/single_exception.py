'''
Handeling exception can be done using following instruction.

try:

     code to be innspected for Exception
     or
     code in which there is chance of getting exception.

except Exception name:

     except block given msg.
'''

x=int(input("enter a numerator:"))
y=int(input("enter denominator:"))

try:
    d=x/y          #d=5/0----> RunTime error ZeroDivisionError
    print("division is:",d)

except ZeroDivisionError:
    print("Denominator cannot be zero, please enter number other than zero")
