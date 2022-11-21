'''
Continue Statement:
==================

Need:
----

If there is need to skip  execution of the code for particular iteration in a loop,
then there is need of continue keyword to acieve it.

e.g

print Hello world for all iterations in loop except fourth ieration.


continue:
it is keyword
it is also associated with if statement.
when continue keyword executed or encountered, loop control goes to
increment/decrement step skipping code for execution after continue
keyword.

'''

for i in range(1,11):
    if i==4:
        continue
    print(i,'-hello world')
