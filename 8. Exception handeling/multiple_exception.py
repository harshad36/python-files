'''
Handeling Multiple Exception
=============================
Handeling exception can be done using following instruction.

try:

     code to be innspected for Exception
     or
     code in which there is chance of getting exception.

except ExceptionName 1:

     except block given msg.

except ExceptionName 2:

     except block given msg.

except ExceptionName 3:

     except block given msg.
.
.
.
except ExceptionName n:

     except block given msg.
'''


try:
    x=int(input("enter a numerator:"))
    y=int(input("enter denominator:"))

    d=x/y          #d=5/0----> RunTime error ZeroDivisionError
    print("division is:",d)

except ZeroDivisionError:
    print("Denominator cannot be zero, please enter number other than zero")
except ValueError:
    print("Enter numerator and denomminator in the digit format.")







