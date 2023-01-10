'''
Logical Operators:
1) logical AND(and)
2) logical OR(or)
3) logical NOT(not)

condition are made up of comparision expression.
AND and OR are binary operators, i.e, they work on two conditions
at a time.


'''

#AND

'''
input(): It is also capable of giving message to user.
         Like print statement.
'''
'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

r=(a>b and a>c)
print(r)
'''

#OR
'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
r=(a>b or a>c)
print(r)

'''

#NOT
'''
It is unary operatot which operates on single condition.

condition         not condition
True               False
False              True
'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
r=not(a>b)
print(r)

