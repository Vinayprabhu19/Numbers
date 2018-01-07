#Calculates either Simple interest or Compound interest based on user's choice
import math
choice=int(input("1)Simple Interest \n2)Compound Interest\n"))
p = int(input("Enter principle : "))
r = int(input("Enter rate : "))
t = int(input("Enter time : "))
#Simple
if choice==1 :
    tax=p*r*t/100
    print("Simple Interest %.2f"%tax)
#Compound
else:
    tax=p*math.pow((1+r/100),t)-p
    print("Compound Interest %.2f"%tax)


