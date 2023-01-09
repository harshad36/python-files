class customer:
    def __init__(self):
        self.bname="SBI"
        self.ifsc="SBIN123"
        self.loc="Eclass"
    def getdata(self):
        self.name=input("Enter customer name:")
        self.mob=input("Enter costumer mobile no:")
        self.bal=float(input("enter accoout balane:"))
    def display(self):
        print("Bank Details")
        print("-------------------------")
        print("Bank name is:",self.bname)
        print("Bank IFSC is:",self.ifsc)
        print("Bank loc is:",self.loc)
        print()
        print("Costumer Details")
        print("---------------------------------")
        
        print("Costumer Name :",self.name)
        print("Costumer Mob No:",self.mob)
        print("COstumer Balance is:",self.bal)

c1=customer() #object created==> constructor is called
c1.getdata()
c1.display()
print()
c2=customer()
c2.getdata()
c2.display()
