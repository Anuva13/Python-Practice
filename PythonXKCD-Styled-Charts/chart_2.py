import matplotlib.pyplot as plt
def main():
    
    categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
    values = [23, 17, 35, 29]

    with plt.xkcd():
        fig, ax = plt.subplots()
        ax.bar(categories, values, color='skyblue')
        ax.set_title("Fruit Popularity Contest")
        ax.set_ylabel("Votes")

        for i, v in enumerate(values):
            ax.text(i, v + 1, str(v), ha='center')

        plt.tight_layout()
        plt.show()
        
if (__name__) == "__main__":
    main()