# Write a program to check whether the string is a palindrome
def main():
    a = input ("Enter String 1 \n")
    c = input("Enter a number\n")
    palindromestring(a)
    palindromenumber(c)

def palindromestring(a):
    b = a[::-1]
    if (a == b):
        print ("The String is Palindrome")
    else:
        print ("The String is not Palindrome")

def palindromenumber(c):
    b = c[::-1]
    if (c == b):
        print ("The number is Palindrome")
    else:
        print ("The numberis not Palindrome")

if __name__ == "__main__":
    main()
