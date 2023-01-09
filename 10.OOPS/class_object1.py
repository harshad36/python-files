'''
Data member and Methods 

'''

class student:
    def getdata(self):
        self.name=input("Enter student name:")
        self.rno=input("Enter student roll number:")
    def display(self):
        print("Student Name is:",self.name)
        print("Student Roll number:",self.rno)
s1=student()

s1.getdata()
s1.display()

s2=student()
s2.getdata()
s2.display()

'''
              self=s1
                 |
         -----------------
        |                 |
        name             rno
     itvedant            35        
  
              self=s2
                 |
         -----------------
        |                 |
        name             rno
      Eclass              45        



'''
