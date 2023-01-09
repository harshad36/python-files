'''
1. required argument
2. Default argument
3. Key value pair argument.
   key=value


   area of rectangle=length x breadth

           3
    ---------------
   |               |
   |               | 2    area=3x2=6
   |               |
    ---------------
'''
def area(l,b):
    print('length of rectangle to be manufacture:',l)
    print('bredth of rectangle to be manufacture:',b)

    area=l*b
    print('area of rectangle is:',area)

#area(10,20)
#area(20,10)
#area(l=10,b=20)
area(b=20,l=10)
