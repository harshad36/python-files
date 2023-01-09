#greatest of three logical

a=int(input('enter a first number:')) #70
b=int(input('enter a second number:'))#50
c=int(input('enter a third number:'))#20,100

if a>b and a>c:    #70>50 and 70>20  T andT = T
    print(a,'is greater')
if b>a and b>c:  #50>70 and 50>20  F and T = T
    print(b,'is greater.')
if c>a and c>b:   #20>70 and 20>50 F and F = F
    print(c,'is greater.')


