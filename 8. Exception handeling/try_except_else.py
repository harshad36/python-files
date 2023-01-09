
'''
try....except and else
======================
else block is executed only when there is no exception.
'''


try:
    x=int(input("enter numerator:"))
    y=int(input("enter denominator:"))
    d=x/y
    
except Exception as x:
    print("Error:",x)
else:
    print("In the else block")
    print("division is:",d)

'''
else block is used to offload try block.

try block should always contains only those lines of code
in which there is chance of getting error.

code lines in which there is no chance of getting run time
error or exception must be in else block.
'''
