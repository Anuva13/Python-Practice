# WAP to perform linear search and if found return the index ofthat elemnt present in the list
def main():
    List = [*range(0,100)]
    Num = int(input("Enter the number to be searched in the list\n"))
    i = -1
    
    for Element in List:
        
        if (Num == Element):
            i = List.index(Element)
            
    if(i>=0):
        print(f"Index of the number found in the list is {i}")
    else:
        print("Number not found")
    
if __name__ == "__main__":
    main()