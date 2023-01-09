'''
A number is entered by User. Write a program to check whether
number is even or odd number.

even: The number which is completely divisible by 2.
      Since it is completely division its remainder of
      the division is Zero.
      opertor:%


step1:start
step2:message to user.=> print()
step3:store that input in variable.=>input()
step4:calculate remainder
step5:if remainder is equal to 0 then it is even
step6:if remainder is not equal to 0 then it is odd..
step7:stop


'''

n=int(input('enter a number:'))
r=n%2
if r==0:
    print('number is even number.')

else:
    print('number is odd number.')
