'''
A character is entered by user,write a program to check
whether that character is equal to a or b or c.

'''

ch=input('enter a character:')
if ch=='a' or ch=='b' or ch=='c':
    print('character found!!')
else:
    print('not found.')

#a==a or a==b or a==c    T or T or T===> T
# q==a or q==b or q==c    F or F or F ===> F
