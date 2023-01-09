'''
Readlines():

This method read files line by line and return list of lines
'''



fp=open("data.txt","r")
d=fp.readlines()

print("data in the file:")
print(d)

print(d[0])
print(d[1])
print(d[2])

print("using for loop")

for x in d:
    print(x)
