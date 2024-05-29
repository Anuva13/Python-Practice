def main():
    List_1 = [1,2,3,4,5,6,7]
    List_2 = ['Ram', 'Shyam', 'Jodhu', 'Modhu']
    List_3 = [1,2,3.4,5.6,'Hawaii', 'Belgium']
    List_4 = list ("HelloWorld")
    new_list = [List_1,List_2,List_3,List_4]
    List_5 = [1,4,5,7,8]
    List_6 = [11,12,13,14,15]


    l1 = len(List_1)
    print(l1)
    l2 = len(List_2)
    print(l2)
    l3 = len(List_3)
    print(l3)
    l4 = len(List_4)
    print(l4)
    print(List_4)
    print(new_list)
    l5 = len(List_5)
    print("l5=", l5)
    l6 = len(List_6)

    increament(List_1,l1) 
    concatenate(List_1,List_2)
    addlistelements(List_5,List_6,l5,l6)

def increament(List_1,l1):
    i=0
    while(i<l1):
        List_1[i] = List_1[i]+5
        i = i+1
    print(List_1)

def concatenate(List_1,List_2):
    new_List2 = []
    new_List2 = List_1+List_2
    print (new_List2)

def addlistelements(List_5,List_6,l5,l6):
    i=0
    j=0
    while (i<l5 or j<l6):
        new_List3.append(List_5[i] + List_6[j])
        i=i+1
        j=j+1
        
    print(new_List3)


if __name__ == "__main__":
    main()