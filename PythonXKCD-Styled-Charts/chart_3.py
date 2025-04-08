import pandas as pd
import cutecharts.charts as ctc
def main():
    
    
    df = pd.read_csv('/Users/snehashish/Python-Practice/PythonXKCD-Styled-Charts/Data/salary.csv')
    df.dropna(inplace=True) # deleting the missing values
    print(df.head())

    gender = df['Gender'].value_counts().to_frame(name="values")
    print(gender)
    
    # Create a pie chart titled "Gender of Respondents"
    chart = ctc.Pie("Gender of Respondents")

    # Configure chart options: labels, color palette, and inner radius
    chart.set_options(
            labels=list(gender.index),
            inner_radius=0,  # 0 means a full pie (not a donut chart)
            colors=['#66C2A5', '#FC8D62', '#8DA0CB'],  # Custom pastel palette
            )

    # Add data series from the gender DataFrame
    chart.add_series(list(gender['values']))

    # Load necessary JavaScript libraries (only needed on the first chart render)
    chart.load_javascript()

    # Render chart to a standalone HTML file
    chart.render("gender_pie_chart.html")
    
if (__name__) == "__main__":
    main()