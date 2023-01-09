'''
x=10
print("data type of x is:",type(x))

class student:
    def greet(self):
        print("Good evening")
s1=student()
print("data type of s1 is:",type(s1))

'''
'''
Conclusion:
Data type of variable is built in datatype i.e int,float
Data type of object is classname.
In above program data type of object s1 is classname=>student.

'''

'''
x is variable of built in Data type.
s1 object is variable of User defined datatype.

x=10

In a single line, x variable is defined[memory allocate] and it
is initialize to value 10.


                      ------------
                     |    10      |
                     |            |
                       ----------
                          x
                          
If there is need to initialize object at its creation, then
there is need of constructor.
'''
'''
1)Constructor is a special method or function which is used
  to initialize object at the time of its creation.


'''


'''
1)Constructor is a special method or function which is used
  to initialize object at the time of its creation.
2)It has fixed name as __init__().
3)Constructor is always called automatically when object
  of the class is created.
'''
class customer:
    def __init__(self):
        print("Constructor is called...")

c1=customer()
c2=customer()





