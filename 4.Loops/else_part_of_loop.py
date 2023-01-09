'''
while loop:
===========

Syntax:

initialization

while condition

     body of while loop

     increment/decrement

else:
    else part of while loop

----------------------------------------

For loop
=========
Syntax:

for var in range(start,stop,step):
            body of for loop
else:
      else part of for loop

else part isexecuted when loop condition become false or terminate.
'''

'''
for i in range(1,6,1):
    print(i,'in for loop body')
else:
    print('in else part of for loop')
'''

for i in range(1,6,1):
    if i==3:
        break
    print(i,'in for loop body')
else:
    print('in else part of for loop')






    
