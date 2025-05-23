import pandas as pd
import cutecharts.charts as ctc
def main():
    
    
    df = pd.read_csv('/Users/snehashish/Python-Practice/PythonXKCD-Styled-Charts/Data/salary.csv')
    df.dropna(inplace=True) # deleting the missing values
    print(df.head())

    # top five cities by the number of respondents in the survey
    cities = df['City'].value_counts()[:5].to_frame(name='values')
    print(cities)
    
    # Create a doughnut chart titled "Top 5 cities by the number of respondents"
    chart = ctc.Pie("Top 5 cities by the number of respondents")

    chart.set_options(
    labels=list(cities.index),
            inner_radius=0.5,
            colors=['#FFF1C5','#F7B7A3','#EA5F89','#9B3192','#57167E','#47B39C','#00529B'],
            )
    chart.add_series(list(cities['values'])) 

    # Calling the load_javascript function when rendering chart first time.
    chart.load_javascript()
    # Render chart to a standalone HTML file
    chart.render("cities_doughnut_chart.html")
    
if (__name__) == "__main__":
    main()