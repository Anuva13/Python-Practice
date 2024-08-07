def main():
    import random
    import time
    
    print(
    """
    ========================================================================================================================
    *********************** Guess The Number Game *****************************
    Please enter a number between the range 1-50!    
    =========================================================================================================================
    """)
    
    number = random.randint(1,50)
    numberofGuesses = 0
    
    name = input("What is your name\n")
    
    print("I am thinking of a whole number between 1 to 50! Can you guess what it is?")
    while (numberofGuesses < 8):
        try:
            guess = int(input("Take a guess:\n"))
            numberofGuesses = numberofGuesses +1
            guessesLeft =  8 - numberofGuesses
            print("Checking...........")
            time.sleep(1)
            
            if (guess < number):
                print("Your guess is too low! You have "+ str(guessesLeft) + " guesses left!")
            if (guess > number):
                print("Your guess is too high! You have "+ str(guessesLeft) + " guesses left!")
            if (guess == number):
                break
        except ValueError:
            print("Please enter a valid number!\n")
        else:
            if (guess < 1) or (guess > 50):
                print("Please enter a number between 1-50!\n")
                
    if (guess == number):
        print("Congratulations! You guessed the number in " + str(numberofGuesses) + " tries: ")
    else:
        print("Sorry the number I was thinking was: "+ str(number))
        
if __name__ == "__main__":
    main()  
        
    
    
    