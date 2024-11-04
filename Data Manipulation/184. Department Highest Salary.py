import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df_max=employee.groupby('departmentId')['salary'].max().reset_index()
    df_joined=pd.merge(df_max,department,how='inner',
    left_on='departmentId',right_on='id')
    df_joined_emp=pd.merge(df_joined,employee,how='inner',
    left_on=['departmentId','salary'],right_on=['departmentId','salary'],
    suffixes=('_d','_e'))
    result=pd.DataFrame({
        'Department': df_joined_emp['name_d'].to_list(),
        'Employee': df_joined_emp['name_e'].to_list(),
        'Salary': df_joined_emp['salary'].to_list()
    })
    return result

    
