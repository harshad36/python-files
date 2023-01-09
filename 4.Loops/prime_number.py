'''
Prime number:
============

a number which is completely divisible by 1 and itself is called as prime number.

n=7

1   2,3,4,5,6       7
    ---------

    excluding 1 and 7 check whether any number completely divides 7 so none of in between
    numbers completely divides 7, thus it is prime number.


    conclusion:
    ----------

    excluding 1 and last number, if any one number completely divides that number given by user,
    then that number is a non-prime number

    if no one completely divide that number then it is called as prime number
    
'''

n=int(input('enter number:'))
for i in  range(2,n,1):
    r=n%i
    if r==0:
        print(n,'is non-prime number')
        break
else:
    print(n,'is prime a number')
'''
n=5

i   i in[2,3,4]  r=5%i   r==0   i=i+1
2   2 in[]T      r=5%2=1 1==0F  i=2+1=3
3   3 in[]T      r=5%3=2 2==0F  i=3+1=4
4   4 in[]T      r=5%4=1 1==0F  i=4+1=5
5   5 in[]F => Completed all iterations

n=7
i   i in[2,3,4,5,6]  r=7%i   r==0   i=i+1
2   2 in[]T          r=7%2=1 1==0F  i=2+1=3
3   3 in[]T          r=7%3=2 2==0F  i=3+1=4
4   4 in[]T          r=7%4=3 3==0F  i=4+1=5
5   5 in[]T          r=7%5=2 2==0F  i=5+1=6
6   6 in[]T          r=7%6=1 1==0F  i=6+1=7
7   7 in[]F
'''
