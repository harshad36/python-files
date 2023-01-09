'''
Handeling any exception with exception parent class.
'''



try:
    x=int(input("enter a numerator:"))
    y=int(input("enter denominator:"))

    d=x/y          #d=5/0----> RunTime error ZeroDivisionError
    print("division is:",d)

except Exception as e:
    #print("Somethinng went wrong!!!",e)
    print("Error:",e)
