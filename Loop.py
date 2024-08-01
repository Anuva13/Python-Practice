def main():
    List_1 = [1,2,3,4,5,6]
    
    forloop1(List_1)
    forloop2(List_1)
    forloop3(List_1)
    rangefunc()
    forlooppattern1()
    forlooppattern2()
    

def forloop1(List_1):
    for Element in List_1:
        print(Element)
        
def forloop2(List_1):
    Sum=0
    for Element in List_1:
        Sum+=Element
        print("Sum:{}  Element:{}".format(Sum,Element))
    print(Sum)
    
def forloop3(List_1):
    for Element in List_1:
        if(Element%2==0):
            print(f"Element {Element} is even")
            
def rangefunc():
    print(*range(0,15))
    print("Even numbers in the range 0-100: \n")
    print(*range(0,100,2))
    
def forlooppattern1():
    for i in range(0,10):
        print(i * "+")
        
def forlooppattern2():
    for i in range(10,0,-1):
        print(i * "+")
        
if __name__ == "__main__":
    main()
        