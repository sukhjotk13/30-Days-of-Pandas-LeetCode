import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    grouped=daily_sales.groupby(['date_id','make_name']).agg(
        unique_leads=('lead_id','nunique'),unique_partners=('partner_id','nunique')
    )
    grouped=grouped.reset_index()
    return grouped[['date_id','make_name','unique_leads','unique_partners']]
