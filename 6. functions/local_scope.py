def scope_variable():
    x=10
    print('value of variable inside of function:',x)

scope_variable()

print('value of variable outside of function:',x)

'''
Variable defined in the function or in a scope has life or accessibilty to its
value within that scope only, it cannot be accessed outside that scope.
This type of variable is called as local variable.
'''
