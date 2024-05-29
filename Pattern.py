def main():
    a = "*"
    i = 0
    j = 5
    print("Right angle triangle\n")
    pattern1(a,i)
    print("\n")
    print("Inverted triangle\n")
    pattern2(a,j)
    print("\n")
    print("Equilateral triangle\n")
    pattern3(a,i)
    print("Inverted equilateral triangle\n")
    pattern4(a,i)

def pattern1(a,i):
    while(i<=5):
        
        print(f"{i*a}\t")
        i = i+1

def pattern2(a,j):
    while(j>=0):
        
        print(f"{j*a}\t")
        j = j-1

def pattern3(a,i):
    space = " "
    k=5
    l=1
    while(l<=5):
        
        print(f"{space*(k-3)}{l*a}\t")
        k = k - 1
        l = l + 2

def pattern4(a,i):
    space = " "
    k=0
    l=5
    while(l>=0):
        
        print(f"{space*k}{l*a} \t")
        k = k + 1
        l = l - 2 


if __name__ == "__main__":
    main()
