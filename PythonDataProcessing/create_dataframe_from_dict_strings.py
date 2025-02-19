import pandas as pd
def main():
    
    data = """[
    {"Name": "Lola", "Age": 3},
    {"Name": "Bailey", "Age": 6},
    {"Name": "Donna", "Age": 10}
    ]"""
    
    df = pd.DataFrame(eval(data))
    print(df)
    
if (__name__) == ("__main__"):
    main()