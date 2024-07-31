def main():
    password = "Anuva"
    Input_password = input("Enter your password\n")
    if(Input_password==password):
        print("Logging in....")
    else:
        print("Incorrect password. Please try again")
        print ("All done")
if __name__ == "__main__":
    main()