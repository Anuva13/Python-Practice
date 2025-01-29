def main():
    List = [32,1,6,4,98]
    length = len(List)
    
    Bubblesort(List, length)
      
def Bubblesort(List, length):
    
    for index in range (length):
        
        for element in range (0, length - index - 1):
            if List[element] > List[element+1]:
                temp = List[element]
                List[element] = List[element+1]
                List[element+1] = temp
    print(List)
              
if __name__ == "__main__":
    main()