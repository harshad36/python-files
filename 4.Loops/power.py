'''
A number and its power is entered by the user. Write a program
to find one number raised to another number.

e.g:
n=2
p=3

2^3=8

t=2*2*2

       2 * 2 *  2
       -----
         4   *  2
         --------
            8
2^5
t=2*2*2*2*2

       2 * 2 * 2 * 2 * 2
       -----
         4   * 2
         -------
             8   * 2
             -------
                16   * 2
                --------
                   32

Note: Loop repeatation is govern by power.
loop
initialization:i=1
condition     :
incre/decre   :
2^5
       
         t=1
       2 t=t*2=1*2=2
       4 t=t*2=2*2=4
       8 t=t*2=4*2=8   =====>
       16t=t*2=8*2=16
       32t=t*2=16*2=32

'''

n=int(input('enter a number:'))
p=int(input('enter a power:'))
i=1
t=1
while i<=p:
    t=t*n
    i+=1
print(t)




'''
n=2  p=3
i    t     i<=p      t=t*n        i+=1
1    1     1<=3 T    t=1*2=1      1+1=2
2    2     2<=3 T    t=2*2=4      2+1=3
3    4     3<=3 T    t=4*2=16     3+1=4
4    16    4<=3 F   loop stop
'''
