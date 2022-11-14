'''
factorial of number entered by User.
===================================

step1: Example

  5!=5*4*3*2*1    4!=1*2*3*4
  or
  5!=1*2*3*4*5

      1 * 2 * 3 * 4 * 5
      -----
        2   * 3
         -----
           6    * 4
            -------
              24    * 5
               --------
                  120
repeatition => multiply and store
        solution    => loop

step2:
       initialization:i=1
       condition     :i<=5  i.e i<=n
       incre/decr    :i+=1


step3:
           f=1 i
         1 f=f*1=1*1=1
         2 f=f*2=1*2=2
         6 f=f*3=2*3=6  ====> f=f*i
        24 f=f*4=6*4=24
        120f=f*5=24*5=120
'''
n=int(input('enter number:'))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print('factorial of',n,'is',fact)


'''
n=5
i fact  i<=n   fact=fact*i  i+=1   fact
1  1    1<=5T  fact=1*1     1+1=2   1
2  1    2<=5T  fact=1*2     2+1=3   2
3  2    3<=5T  fact=2*3     3+1=4   6
4  6    4<=4T  fact=6*4     4+1=5   24
5  24   5<=5T  fact=24*5    5+1=6   120
6  120  6<=5F  loop stop
'''
