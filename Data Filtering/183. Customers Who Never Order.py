import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(customers,orders,how='left',left_on='id',right_on='customerId',suffixes=('_customer', '_order'))
    df1=df[df['id_order'].isnull()]
    return df1[['name']].rename(columns={'name':'Customers'})
    
