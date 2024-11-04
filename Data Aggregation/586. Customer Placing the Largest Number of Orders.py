import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result=orders.groupby('customer_number')['order_number'].count()
    result=result.reset_index()
    req=result[result['order_number']==result['order_number'].max()]
    return req[['customer_number']]
