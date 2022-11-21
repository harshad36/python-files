'''
Break keyword:

Need of break keyword:
======================

ideally loop stop working when condition become false.
If there is need to stop or terminate the loop even if the loop condition
is true, then there is need of break keyword.


Break keyword [It has reserved meaning]
=======================================
Break is a keyword which is used to stop or terminate the lop even if the
loop condition is True.
Break is always associated with if statement in loop i.e break keyword does
its work to terminate the loop based on certain condition.

'''
for i in range(1,11):
    if i==5:
        break
    print(i)
print('out of the loop')
