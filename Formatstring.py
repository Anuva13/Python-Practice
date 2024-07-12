def main():

    a = input ("Enter a string\n")
    

    length(a)
    seperator(a)
    space(a)
    formatting()
    padding(a)
   
def length(a): 
    l = len(a)
    print("The length of the string is:", l)

def seperator(a):
    print(a,a,a, sep = " . ")

def space(a):
    print(* a, sep="#")

def formatting():
    Firstname = input("Enter your firstname\n")
    Age = int(input("Enter your age\n")) 
    print ("My name is {Firstname}.\nI am {Age} years old.".format(Firstname,Age))

def padding(a):
    print ('{:>10}'.format('test'))
    print ('{:10}'.format('test'))
    print ('{:.3}'.format('Jamaica'))
       

if __name__ == "__main__":
    main()