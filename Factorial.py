def main():
    Num = int(input("Enter a number for which you want to find the factorial\n"))
    fact = 1
    factorial(Num,fact)
    
def factorial(Num,fact):
    
    if (Num == 0):
        print(f"Factorial = {fact}")
    else:
        while(Num>0):
            fact = fact*Num
            Num = Num-1
        print(f"Factorial = {fact}")
        
if __name__ == "__main__":
    main()