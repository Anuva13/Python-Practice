#WAP to perform calculator operations
def main():
    
    print("Choice 1 is Addition")
    print("Choice 2 is Subtraction")
    print("Choice 3 is Multiplication")
    print("Choice 4 is Division")
    
    choice = int(input("Enter a choice from 1/2/3/4\n"))
    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))
    
    if(choice==1):
        print(f"Addition = {num1+num2}")
    elif(choice==2):
        print(f"Subtraction = {num1-num2}")
    elif(choice==3):
        print(f"Multiplication = {num1*num2}")
    elif(choice==4):
        if(num2 ==0):
            print("Invalid result as denominator with 0 is undefined")
        else:
             print(f"Division = {num1/num2}")
        
if __name__ == "__main__":
    main()