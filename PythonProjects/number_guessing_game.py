import random
def main():
    
    print("🎯 Welcome to the Number Guessing Game!")
    
    while True:
        # Random number between 1 and 100
        selected_number = random.randint(1,100)
        # User gets only 5 attempts
        attempt = 5
        
        print("\nI have selected a number between 1 and 100. Try to guess it!")
        
        while attempt > 0:
            try:
                guess = int(input(f"Attempts left: {attempt} - Enter your guess: "))
                
                if guess < 1 or guess > 100:
                    print("🚫 Please enter a number between 1 and 100.")
                
                elif guess < selected_number:
                    print("📉 Too low! Try again.")
                
                elif guess > selected_number:
                    print("📈 Too high! Try again.")
                
                else:
                    print(f"🎉 Congratulations! You guessed the number {selected_number} in {attempt} attempts!")
                    break
            
                attempt = attempt - 1
                
                if attempt == 0:
                    print(f"❌ Out of attempts! The correct number was {selected_number}. Better luck next time!")
                          
            except ValueError:
                print("⚠️ Invalid input! Please enter a valid number.")
                
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != 'yes':
            print("👋 Thanks for playing! Goodbye!")
            break
            
if __name__ == "__main__":
    main()

                
                
                
                