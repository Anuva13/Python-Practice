import pandas as pd
def main():
    
    # Read CSV file
    df = pd.read_csv("./ExampleCSV/I_Sample1.csv")

    # Save as a .dat file (tab-separated format)
    df.to_csv("./ExampleCSV/O_Sample_Employee_Data1.dat", sep="\t", index=False, engine="python")  # Use '\t' for tab, or change delimiter as needed

    print("CSV successfully converted to .dat")
 
if (__name__) == "__main__":
    main()
