#WAP Fifo using Dict
def main():
    List = [1,2,3,4]
    print(f"Current stack is {List}")
    Num = int(input("Enter a number\n"))
    choice = int(input("Enter a choice of operation \n 1. Push\n 2. Pop\n"))
    
    if(choice==1):
        push(List,Num)
    elif(choice==2):
        pop(List)
    
    
def push(List,Num):
    List.insert(0,Num)
    print(List)
    
def pop(List):
    del List[0]
    print(List)
    
if __name__ == "__main__":
    main()
