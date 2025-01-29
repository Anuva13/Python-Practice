def main():
    List = [1,2,3,4]
    Num = int(input("Enter the number\n"))
    print(f"Current stack is {List}")
    #print(f"New stack is {List.append(Num)}")
    print(List.pop())
    List.append(Num)
    print(List)
    

    
if __name__ == "__main__":
    main()