# import datetime
# import os
# import time
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR2=os.path.dirname(os.path.abspath(__file__))
# t=os.path.join(BASE_DIR2,'templates')
# print(t)
# a=datetime.datetime.now()
# print(a)
#
# class p1:
#     x=10
#     _y=20
#     __z=30
#
# print(p1.x)
# print(p1._y)
# #print(p1.__z) we will get error if we put this code because it is producet we access that using nameing function
# #create object for name using name function
# p=p1()
# print(p._p1__z)

class account:
    def __init__(self,name,bal,min_bal):
        self.name=name
        self.bal=bal
        self.min_bal=min_bal

    def deposit(self,amount):
        if amount>0:
            self.bal=self.bal+amount
        else:
            print("check enter amount")

    def withdraw(self,amount):
        if self.bal-amount>self.min_bal:
            self.bal=self.bal-amount
        else:
            print("insufficient")
    def printstatement(self):
        print(self.bal)

class saving(account):

    def __init__(self,name,bal):
        super().__init__(name,bal,min_bal=0)
    def __str__(self):
        return f"{self.name} {self.bal}"

c=saving("phantom",100000000000000000000000000000000000000000000)
print(c)
c.deposit(0)
c.printstatement()