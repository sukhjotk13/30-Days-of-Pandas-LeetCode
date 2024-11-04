import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time_spent']=employees['out_time']-employees['in_time']
    result=employees.groupby(['event_day','emp_id'])['time_spent'].sum()
    result=result.reset_index()
    result.rename(columns={'time_spent':'total_time','event_day':'day'},inplace=True)
    return result[['day','emp_id','total_time']]
