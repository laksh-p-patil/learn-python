import math

def percentage(attended,total):
    if attended<0 or total <=0:
        print("Total number of classes must be greater than zero while attended classes must be zero or greater. Please re-enter the values")
    elif attended>total:
        print("Number of attended classes cannot be greater than total number of classes")
    else:
        return (attended/total)*100

def skipping(attended,total):
    if result>=75:
        x=(4*attended-3*total)/3
        print("Number of classes you can skip is ",math.floor(x)," to get 75% attendance")
    else:
        y=3*total-4*attended
        print("Number of classes you have to attend is",y," to get 75% attendance")

attended = int(input("Enter the number of classes attended: "))
total = int(input("Enter the total number of classes: "))
result = percentage(attended,total)

if result is None:
    pass
else:
    print(f"You attended {result:.1f}% of the classes.")
    skipping(attended,total)