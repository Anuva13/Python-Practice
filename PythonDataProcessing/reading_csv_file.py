import csv
def main():
    
    f = open("./ExampleCSV/I_Sample1.csv")
    
    read(f)
    write()
    
def read(f):
    csv_f = csv.reader(f)
    for row in csv_f:
        Name, Age, Salary, Department = row
        print("Name: {}, Age: {}, Salary: {}, Department: {}".format(Name, Age, Salary, Department))

f.close()

def write():
    hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
    with open('hosts.csv', 'w') as hosts_csv:
        writer = csv.writer(hosts_csv)
        writer.writerows(hosts)    
    
if __name__ == "__main__":
    main()