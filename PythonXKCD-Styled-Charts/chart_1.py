import matplotlib.pyplot as plt

# Activate XKCD mode
with plt.xkcd():
    # Create your figure and axis
    fig, ax = plt.subplots()

    # Sample data
    years = [2019, 2020, 2021, 2022, 2023]
    values = [100, 120, 115, 130, 170]

    # Plot the data
    ax.plot(years, values, marker='o')
    ax.set_title('My Growth Over the Years')
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')

    # Add some comic-style annotation
    ax.annotate(
        'Big jump!',
        xy=(2023, 170),
        xytext=(2021.5, 160),
        arrowprops=dict(arrowstyle='->')
    )

    plt.tight_layout()
    plt.show()
