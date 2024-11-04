import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouped = activities.groupby('sell_date').agg(
    products=('product', lambda x: ','.join(sorted(set(x)))), num_sold=('product', 'nunique'))
    grouped=grouped.reset_index()
    return grouped[['sell_date','num_sold','products']]
