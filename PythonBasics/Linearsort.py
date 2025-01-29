# WAP to sort a list using Linear sorting technique
def main ():
    List_1 =[7,54,5,31,67,35]
    List_2 = [* range(min(List_1),max(List_1)+1)]
    common_elements = [element for element in List_2 if element in List_1]
    print(common_elements)
                  
if __name__ == "__main__":
    main()