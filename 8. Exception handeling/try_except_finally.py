'''
try...except....finally

finally block is excuted in both situation
1) If there is exception
2) If these is no exception.
'''


try:
    x=int(input("enter a numerator:"))
    y=int(input("enter denominator:"))

    d=x/y          #d=5/0----> RunTime error ZeroDivisionError
    print("division is:",d)

except Exception as e:
    #print("Somethinng went wrong!!!",e)
    print("Error:",e)

finally:
    print("inside Finally Block")



'''

Whenever a transation of inserting record, retrieve records
update record and delete record with the database is
completed, it is a good practice to close connection of
your code with database, so that data is secured.

      python ---Connection----> Database [to perform operations]

And even if exception arises, then connection to the database
must be closed.

'''

'''
