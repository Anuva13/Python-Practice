## Finding Prime Numbers
def main():
    User_Input_Num = int(input("Enter a number \n"))
    prime(User_Input_Num)
    
def prime(User_Input_Num):
    if User_Input_Num <= 1:
        print(f"{User_Input_Num} is not a prime number.")
        
    if User_Input_Num <= 3:
        print(f"{User_Input_Num} is a prime number.")
        
    if User_Input_Num % 2 == 0 or User_Input_Num % 3 == 0:
        print(f"{User_Input_Num} is not a prime number.")
        
    i=5
    while i * i <= User_Input_Num:
        if User_Input_Num % i == 0 or User_Input_Num % (i + 2) == 0:
            print(f"{User_Input_Num} is not a prime number.")
            i += 6
        else:
            print(f"{User_Input_Num} is a prime number.")
            
if __name__ == "__main__":
    main()

        
    
        
        
