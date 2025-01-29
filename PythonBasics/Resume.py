def main():
    
    User_input_string = input("enter a string\n")
    User_input_character_old = input("enter the character which you want to replace in the string\n")
    User_input_character_new = input("enter the character with which you want to replace the existing character in the string\n")
    User_input_string_lower = User_input_string.lower()
    Updated_string = User_input_string_lower.replace(User_input_character_old,User_input_character_new)
    print(Updated_string.capitalize())
    
if __name__ == "__main__":
    main()
    