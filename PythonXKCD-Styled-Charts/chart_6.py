import pandas as pd
import cutecharts.charts as ctc
def main():
    
    
    df = pd.read_csv('/Users/snehashish/Python-Practice/PythonXKCD-Styled-Charts/Data/salary.csv')
    df.dropna(inplace=True) # deleting the missing values
    print(df.head())
    
    #Filtering salary and experience details of only Software Engineers
    se = df[df['Position '] == 'Software Engineer']
    se.rename(columns = {'Yearly brutto salary (without bonus and stocks) in EUR': 'Salary'}, inplace=True)

    salary_exp = se.groupby(['Total years of experience'])['Salary'].median().to_frame().reset_index()
    salary_exp[['Total years of experience','Salary']] = salary_exp[['Total years of experience','Salary']].astype(int)
    salary_exp.sort_values('Total years of experience',inplace=True)
    print(salary_exp[:5])
    
    # Create Line chart for plotting median compensation by years of experience
    chart = ctc.Line("Median compensation by years of experience")
    chart.set_options(
    labels=list(salary_exp['Total years of experience']), 
    x_label="Experience in Years",
    y_label="Salary in EUR",
    colors=['#EA5F89'])
    chart.add_series("Salary", list(salary_exp['Salary'])) 

    # Calling the load_javascript function when rendering chart first time.
    chart.load_javascript()
    # Render chart to a standalone HTML file
    chart.render("median_compensation_line_chart.html")
    
if (__name__) == "__main__":
    main()