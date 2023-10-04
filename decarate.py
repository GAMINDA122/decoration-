num1=float(input("Enter your 1st number : "))
num2=float(input("Enter your 2nd number : "))

def divide (a,b):
    if b==0:
        a,b=b,a
    return a/b


print("Answer is ",divide(num1,num2)) 
