#Python Programming Basics & Data Structures Assignment
def main():
    First_name = input("Enter first name\n")
    Last_name = input("Enter last name\n")
    Radius = int(input("Enter the radius of the circle\n"))
    Pi = 3.14
    First_num = int(input("Enter first number\n"))
    Second_num = int(input("Enter second number\n"))
    Weight = int(input("Enter weight in kg\n"))
    Height = float(input("Enter height in m\n"))
    Num = int(input("Enter a number to check if its odd or even\n"))
    
    
    reverse(First_name,Last_name)
    circle(Radius,Pi)
    sphere(Pi)
    swap(First_num,Second_num)
    bmi(Weight,Height)
    OddorEven(Num)
    
def reverse(First_name,Last_name):
    Reverse_first_name = First_name[::-1]
    Reverse_last_name = Last_name[::-1]
    
    print(Reverse_last_name+" "+Reverse_first_name)
    
def circle(Radius,Pi):
    print("Area of circle=",Pi*Radius*Radius)
    
def sphere(Pi):
    r=5
    Volume = (4/3)*Pi*r*r*r
    print(f"Volume of the sphere with radius {r} = {Volume}")
    
def swap(First_num,Second_num):
    c=First_num
    First_num=Second_num
    Second_num=c
    print(f"After swap first number is {First_num} and second number is {Second_num}")
    
def bmi(Weight,Height):
    b = Weight/(Height*Height)
    print(f"BMI of this person is {b}")
    
def OddorEven(Num):
    if(Num>0):
        if(Num%2==0):
            print(f"Number {Num} is Even")
        else:
            print(f"Number {Num} is Odd")
    else:
        print(f"Number {Num} is invalid number type")
    
if __name__ == "__main__":
    main()
    
