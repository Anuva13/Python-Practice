# write a program to do all math ops of python by taking user input
def main():
    a = int(input("Enter first number \n"))
    b = int(input("Enter second number \n"))

    add (a,b)   
    sub (a,b)
    mul (a,b)
    div (a,b)
    sqrt (a)
    cube (b)


def add(a,b):
    c = a + b
    print (f"Addition = {c}")

def sub(a,b):
    c = a - b
    print (f"Subtraction = {c}")

def mul(a,b):
    c = a*b
    print (f"Multiplication = {c}")

def div(a,b):
    c = a/b
    d = a%b
    e = a//b
    print (f"Division = {c}\nMdulous = {d}\nFloordiv = {e}")

def sqrt(a):
    c = a ** (0.5)
    print (f"Squareroot = {c}")

def cube(b):
    c = b ** (3)
    print (f"Cube = {c}")

if __name__  ==  "__main__":
    main()