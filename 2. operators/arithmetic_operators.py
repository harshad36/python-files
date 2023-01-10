'''
Arithmetic Operators:
+, -, *, /
//, %, **
'''
print("Enter first number: ")
x=input() 
a=int(x)
print("Enter second number: ")
y=input()
b=int(y)

'''
add=a+b
print("Addition is : ",add) 

sub=a-b
print("Subtraction is : ", sub)

mul= a*b
print("Multiplication is : ", mul)

div=a/b
print("Division is : ", div)

'''

'''
// => True Division
      This operator perform division and returns quotient of the division.

                    4  ---> Quotient
9//2 =>          ---------       
  Division ---->2|  9       ----> dividend
                  - 8

                 ---------
                    1  ---> Remainder
'''                    

'''
tdiv=a//b
print("True Division is:",tdiv) # True Division is: 4
'''

'''
%(Modulus operator): This operator perform division and returns remainder.
'''
'''
rem=a%b
print("Remainder is: ",rem) #Remainder is: 1
'''

'''
**: Exponent Operator
    This operator return one number raised to another number.

syntax: n**p

4^2=16
4**2=16
'''

pw=a**b #a is number and b is power
print("Exponent is: ",pw)

