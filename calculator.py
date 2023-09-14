def add(x,y):
    return x+y
def substract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def main():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    print(" the value of sum is: " + str(add(a,b)))
    print(" the value of sum is: " + str(multiply(a,b)))
    print(" the value of sum is:" + str(divide(a,b)))
    print(" the value of sum is:" + str(substract(a,b)))
main()
