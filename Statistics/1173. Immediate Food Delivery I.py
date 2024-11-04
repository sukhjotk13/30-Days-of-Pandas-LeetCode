import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate=delivery[delivery['order_date']==
    delivery['customer_pref_delivery_date']]
    no_of_immediate=len(immediate['delivery_id'])
    total=len(delivery['delivery_id'])
    df=pd.DataFrame({'immediate_percentage': 
    [round((no_of_immediate*100.0/total),2)]})
    return df
