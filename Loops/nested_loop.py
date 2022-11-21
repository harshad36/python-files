'''
Nested Loop
===========

one lop inside another loop is called as nested loop.





There is a outer loop and there is a inner loop.
'''

for i in range(1,4,1):
    print('i=',i)
    for j in range(1,4,1):
        print(j)

'''
                               - -----------------------------
                              |           j loop             |
i   i in [1,2,3]   print(i)   j    j in [1,2,3]  print(j)  j=j+1      i=i+1

1   1  in[]T         1        1    1 in []T         1        2
                              2    2 in []T         2        3
                              3    3 in []T         3        4
                              4    4 in []F                             2

2   2  in[]T         2        1    1 in []T         1        2
                              2    2 in []T         2        3
                              3    3 in []T         3        4
                              4    4 in []F                             3

3   3  in[]T         3        1    1 in []T         1        2
                              2    2 in []T         2        3
                              3    3 in []T         3        4
                              4    4 in []F                             4

4    4 in []F
'''
