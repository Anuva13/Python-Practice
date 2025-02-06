""" def main():

   
    a = "Anuva"
    l = len(a)
    #print("The length of the string is:", l)
    print(1,2,3,4, sep=".")

if __name__ == "__main__":
    main()
"""
    

import importlib.util

def main():

    if importlib.util.find_spec("openpyxl") is not None:
        print("openpyxl is installed")
    else:
        print("openpyxl is NOT installed")
    
if (__name__) == "__main__":
    main()
