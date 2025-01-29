# WAP to alter the value of a key passed by user and print the modified dictionary
def main():
    Dict_1 = {"Name":"Anuva","age":25}
    User_input_value = int(input("Enter the age value to be updated \n"))
    Dict_1["age"] = User_input_value
    print(Dict_1)

if __name__ == "__main__":
    main()