# Swapping Numbers using Pass by value
def main():
    a=2
    b=3
    approach1(a,b)
    approach2(a,b)
    approach3(a,b)

def approach1(a,b):
    c=a
    a=b
    b=c
    print(a)
    print(b)

def approach2(a,b):
    a = a+b
    b = a-b
    a = a-b
    print(a)
    print(b)

def approach3(a,b):
    a,b = b,a
    print(a)
    print(b)

if __name__ == "__main__":
    main()
