
import time
import os
# def fibo():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#
#
# for i in fibo():
#     if os.name=='nt':
#         os.system('cls')
#     else:
#         os.system('clear')
#     time.sleep(1)
#     print((i))

def fun(*a,**b):
    for i in a:
        print(i)
    for i in b:
        print(i)
    print(a)
    print(b)

    for k,v in b.items():
        print(k,":",v)

fun('a','b','c','d','e',x=10,y=20,z=30)
class p1:
    def __init__(self,age,name):
        self.age=age
        self.name=name

    def eat(self):
        print("from p1")

class p2(p1):
    def __init__(self,age,name,emname,emsalary):
        super().__init__(age,name)
        self.emnane=emname
        self.emsalary=emsalary


    def m2(self):
        print("p2")
        print("if want to call first class eat function then press 1 ")
        n=int(input("."))
        if n==1:
            super().eat()
        else:
            print("exiting")
            time.sleep((3))
            return  f"this{self.age} is down"

c=p2(19,'rahul','rahul',800000)
s=c.m2()
print(s)



