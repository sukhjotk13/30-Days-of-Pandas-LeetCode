import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df=employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(df)==1:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else: 
        return pd.DataFrame({'SecondHighestSalary':[df.iloc[1]]})
