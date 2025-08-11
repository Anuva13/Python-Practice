def main():
    
    read()
    readfileblock()
    
def read():
    file = open("./ExampleCSV/I_Sample_txt_file.txt") # The open() function returns a file object which is assigned to the variable file.
    print(file.readline()) # Reads first line
    print(file.readline()) # Reads next line from current position
    print(file.read()) # Reads the remaining lines in the text from the current position
    file.close() # Close the file
    
def readfileblock():
    with open("./ExampleCSV/I_Sample_txt_file.txt") as file:
        print(file.readline())

if __name__ == "__main__":
    main()
    
