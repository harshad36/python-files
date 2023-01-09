n1=int(input('enter first number:'))
n2=int(input('enter second number:'))
def arithmetic(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y

    return add,sub,mul,div
a,b,c,d=arithmetic(n1,n2)
print("addition is:",a)
print("subtraction is:",b)
print("multiplication is:",c)
print("division is:",d)
