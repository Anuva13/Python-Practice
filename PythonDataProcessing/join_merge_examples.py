import pandas as pd
def main():
    
    # Creating DataFrames
    df1 = pd.DataFrame({
        'employee_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'dept_id': [101, 102, 101, 103],
        'manager_id': [3, 3, None, 1]
    })

    df2 = pd.DataFrame({
        'dept_id': [101, 102, 104],
        'dept_name': ['HR', 'Finance', 'IT']
    })
    
    # Inner Join (Only matching dept_id)
    print("> {join}:".format(join="inner join"))
    inner_join = pd.merge(left=df1, right=df2, on='dept_id', how='inner')
    print(inner_join)
    print("\n")
    
    # Left Outer Join (All employees, matching dept_id)
    print("> {join}:".format(join="left outer join"))
    left_outer_join = pd.merge(left=df1, right=df2, on='dept_id', how='left')
    print(left_outer_join)
    print("\n")
    
    # Right Outer Join (All departments, matching dept_id)
    print("> {join}:".format(join="right outer join"))
    right_outer_join = pd.merge(left=df1, right=df2, on='dept_id', how='right')
    print(right_outer_join)
    print("\n")
    
    # Full Outer Join (All records from both tables)
    print("> {join}:".format(join="full outer join"))
    full_outer_join = pd.merge(left=df1, right=df2, on='dept_id', how='outer')
    print(full_outer_join)
    print("\n")
    
    # Self Join (Employees and their manager)
    print("> {join}:".format(join="self join"))
    self_join = pd.merge(left=df1, right=df1, left_on="manager_id", right_on="employee_id", suffixes=('_emp', '_mgr'))
    print(self_join[['name_emp', 'name_mgr']])
    print("\n")
    
    
if (__name__) == "__main__":
    main()