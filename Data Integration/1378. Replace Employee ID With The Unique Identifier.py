import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged_df=pd.merge(employee_uni,employees,how='right',on='id')
    return merged_df[['unique_id','name']]
