'''
range():This function generate list of numbers in a sequence.
syntax:

     range(start,stop,step)

     start=> initialization
     stop => conditon
     step => increment/decrement [positive or negative]
     
'''
'''
x=list(range(1,10,1))
print(x)
'''

'''
x=list(range(2,20,2))
print(x)
'''

#no step
'''
x=list(range(2,20))  default step is 1
print(x)
'''

#no step and start
'''
x=list(range(20))
print(x)             default start is 0
'''

#no start,step and  stop 
'''
x=list(range())      TypeError: range expected at least 1 argument, got 0
print(x)
'''
x=list(range(15,5,-2))
print(x)

#15-2, 13,13-2,11,11-2,9,9-2,7,
