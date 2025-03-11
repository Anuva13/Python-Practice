from sklearn.linear_model import LinearRegression
def main():
    
    X = [[1], [2], [None], [4]]
    y = [3, 4, 5, 6]

    model = LinearRegression()
    model.fit(X, y)  # This will throw an error due to None
    
if (__name__) == "__main__":
    main()
