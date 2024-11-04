import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['category']=accounts['income'].apply(lambda x:"Low Salary" if 
    x<20000 else "Average Salary" if 20000<=x<=50000 else "High Salary")
    categories=["Low Salary","Average Salary","High Salary"]
    df=accounts['category'].value_counts().reindex(
    categories,fill_value=0).reset_index()
    df.columns=['category','accounts_count']
    return df
