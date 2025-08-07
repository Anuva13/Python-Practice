import pandas as pd
def main():
    
    visitors = [1234, 6424, 9345, 8464, 2345]
    errors = [23, 45, 33, 45, 76]
    df = pd.DataFrame({"Visitors": visitors, "Errors": errors}, index = ["Mon", "Tue", "Wed", "Thu", "Fri"])
    print(df)
    print(df["Errors"].mean())
    
if __name__ == "__main__":
    main()