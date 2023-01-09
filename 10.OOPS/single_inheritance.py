'''
Single Inheritance:
==================
The inheritance in which there is only one base class and
one derived class is called as Single inheritance.

                         A base class
                         |
                         |
                         |
                         B Derived class
                         
In class A

method     =>geta()
data member=>a

class B
method      => getb()
data member => b
'''

class A:
    def geta(self): #self=b
        self.a=int(input("enter a  value of a:"))
class B(A):
    def getb(self):
        self.b=int(input("enter a value of b:"))
    def addition(self):
        res=self.a+self.b
        print("Addition is:",res)

b=B()  #object of derived class
b.geta() #geta(b)
b.getb()
b.addition()
