'''
Hybrid inheritance
==================
The inheritance which is the combination of Hirarchical and
multiple inheritance is called as Hybrid Inheritance.

                        A geta() => self.a
                        |
                 -----------------
                |                 |
getb()=>self.b  B                 C  self.c <= getc()
                |                 |
                 ----------------
                        |
                        D addition()
class A:


class B(A):


class C(A):



class D(B,C):
'''


class A:
    def geta(self):
        self.a=int(input("Enter a value of a:"))
class B(A):
    def getb(self):
        self.b=int(input("Enter a vslue of b:"))
class C(A):
    def getc(self):
        self.c=int(input("enter a value of c:"))
class D(B,C):
    def addition(self):
        res=self.a+self.b+self.c
        print("Addtion is:",res)

d1=D()
d1.geta()
d1.getb()
d1.getc()
d1.addition()
