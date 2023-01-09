'''

variable length argument
========================

variable:changing

length:number of argument


'''



def addition(*x):
    
    sum=0
    for i in x:
        sum=sum+i
    print('sumation is:',sum)

addition(20,10)
addition(20,30,40)
addition(20)


#addition(20,30)
#x=(20,30)

'''
i  i  in x    sum=sum+i      i
20 20 in x[T] sum=0+20=20    30
30 30 in xT   sum=20+30=50      --F

summation is:50

'''
#addition(20,30,40)
#x=(20,30,40)

'''
i   i in x    sum=sum+i    i




'''
