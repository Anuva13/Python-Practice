# WAP which takes a number as a input and then based on the number entry it finds out what are the factors of the number
def main():
    User_input_number = int(input("Enter a number\n"))
    factor(User_input_number)
    
def factor(User_input_number):
    fact = 1
    
    while(fact<=User_input_number):
        if(User_input_number%fact==0):
            print(fact)    
        fact=fact+1

if __name__ == "__main__":
    main()
        
        
    