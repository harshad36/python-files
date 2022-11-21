'''
String:
'''


#x='itvedant'

'''x= this is string
multiline string
itevedant e-class learning
string
'''
x='itvedant-eclass'
print(x)
print(type(x))
#len(): This is used to calculate number of characters in the string.

n=len(x)
print('length of x is:',n)


#indexing
'''
Need: To process string character by character , there is need
to access character in the string. Indexing helps you to access
character in the string.
There are two types of indexing
1)Positive indexing
2)Negative indexing

syntax for accessing:
====================
 string_variable[index_number]



Positive index                    x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Negative Index                  
          I   t   v  e   d   a  n   t -  E  c   l  a  s  s 
        -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

        '''
'''
print(x[7])
print(x[11])
#print(x[17])  #IndexError: string index out of range
print(x[-6])
print(x[-15])
'''

#slicing
'''
Need of slicing:
==============
If there is need to extract partial part of the string from
entire string , then use slicing.
1) to reverse string.

syntax:

string_variable[start:stop:step]
                                   x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

Extract vedant word from the give string.

start=>2  stop=>8  step=>1
'''
#x1=x[2:8:1]
#x1=x[10:15:1]
#x1=x[2:8:2]
#x1=x[2:8:]  default step is 1
#x1=x[:8:]  default start is 0
#x1=x[::]# default stop = string end
'''
slicing with negative index

                        Negative Index                  
          I   t   v  e   d   a  n   t -  E  c   l  a  s  s 
          0   1   2  3   4   5  6   7 8  9 10  11 12 13 14
        -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

step=> negative

conclusion:
if step is positive then start=left  end=right
if step is negative then start=right end=left
'''
#x1=x[14:8:-1]
#x1=x[:2:-1]
x1=x[::-1]
print(x1)























