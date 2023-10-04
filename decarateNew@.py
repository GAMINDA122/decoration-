num1 = float(input("Enter your 1st number : "))
num2 = float(input("Enter your 2nd number : "))
def new(func):
    def inside(a,b):
        if b==0:
            a,b=b,a
        return func(a,b)
    return inside

@new
def divide(a,b):
    return a/b



print("Your Answer is ",divide(num1,num2))