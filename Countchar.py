# write a program to count the number of times a letter is appearing in the string
def main():
    a = input("enter a string\n")
    b = input("enter the character for which you want to find its number of occurrence in the string\n")
    c = 0
    l = len(a)
    i = 0

    while (i<l):
        
        if(a[i]==b):
            c = c + 1
        i = i + 1
    print (f"Number of occurrence of letter {b} {c}")

if __name__ == ("__main__"):
    main()



    
