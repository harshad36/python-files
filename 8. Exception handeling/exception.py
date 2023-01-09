'''
Exception
=========

Error: These are faults or mistakes in the program.
there are two types of errors:
1)Compile time error
2) Run time error

Compile time error:
==================
these errors are mainly due to mistakes done in writing the syntac of the code.

Run time error:
================
the errors are occurs during the execution of program are cslled as run time error

Mainly due to user input or importing module which is not there at the location.

stage1:   Error checking stage.
stage2:   Code execution stage.
'''

#import arithmetic----> Run time Error  ModuleNotFoundError: No module named 'arithmetic'
x=int(input("enter a numerator:"))
y=int(input("enter denominator:"))

d=x/y          #d=5/0----> RunTime error ZeroDivisionError
print("division is:",d)


#What is different between Errors and Exception?
 
