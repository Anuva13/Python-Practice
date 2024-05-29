# Print any user wished character of the entered name
def main():
    a = input("Enter a name \n") #Anuva
    b = int(input("Enter the letter number you want to print \n"))  #2
    c = int(input("Enter the range of length of string you want to slice \n"))

    printchar(a,b)
    slicing(a,c)
    reverse(a)

def printchar(a,b):
    print (a[b-1])

def slicing(a,c):
    print(a[0:c-1:2])

def reverse(a):
    print(a[::-1])

if __name__ == "__main__":
    main()