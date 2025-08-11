def main():
    
    read()
    readfileblock()
    capitalisefiletext()
    removeemptyline()
    readfileinmemory()
    
def read():
    file = open("./ExampleCSV/I_Sample_txt_file.txt") # The open() function returns a file object which is assigned to the variable file.
    print(file.readline()) # Reads first line
    print(file.readline()) # Reads next line from current position
    print(file.read()) # Reads the remaining lines in the text from the current position
    file.close() # Close the file
    
def readfileblock():
    with open("./ExampleCSV/I_Sample_txt_file.txt") as file:
        print(file.readline())
        
# learning to iterate with files
def capitalisefiletext():
    with open("./ExampleCSV/I_Sample_txt_file.txt") as file:
        for line in file:
            print(line.upper())
            
def removeemptyline():
    with open("./ExampleCSV/I_Sample_txt_file.txt") as file:
        for line in file:
            print(line.strip().upper())
            
def readfileinmemory():
    file = open("./ExampleCSV/I_Sample_txt_file.txt")
    lines = file.readlines()
    file.close()
    # Here even when the file is closed the file content is in the list i.e. memory and can be used to process
    lines.sort()
    print(lines)
            
if __name__ == "__main__":
    main()
    
