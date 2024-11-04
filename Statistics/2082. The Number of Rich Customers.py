import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich=store[store['amount']>500]
    unique_cust=rich['customer_id'].unique()
    num=len(unique_cust)
    df=pd.DataFrame({'rich_count':[num]})
    return df
