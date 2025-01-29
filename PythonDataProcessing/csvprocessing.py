import pandas as pd
def main():

    # Load CSV file into a DataFrame
    df = pd.read_csv("./ExampleCSV/I_Sample1.csv")

    # Display first 5 rows
    print(df.head())

    # Get basic statistics
    print(df.describe())

    # Filter data (e.g., selecting rows where Age > 30)
    df_filtered = df[df["Age"] > 30]
    print(df_filtered)

    # Save filtered data to a new CSV file
    df_filtered.to_csv("./ExampleCSV/O_Sample1.csv", index=False)
    
if __name__ == "__main__":
    main()